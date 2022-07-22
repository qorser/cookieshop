# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import fields, models
import json
from odoo.exceptions import UserError, ValidationError
import requests
from datetime import datetime, timedelta

class IsiPulsaWizard(models.TransientModel):
    _name = "isi.pulsa.wizard"
    _description = "Isi pulsa denngan menginput data yang diperlukan di bawah ini!"

    name = fields.Char(string="ID IRS")
    irs_pin = fields.Char(string="PIN IRS")
    irs_username = fields.Char(string="Username IRS")
    irs_password = fields.Char(string="Password IRS")
    product_code = fields.Char(string="Kode Produk")
    phone_number = fields.Char(string="Nomor Tujuan")
    trx_type = fields.Char(string="Tipe Transaksi (Khusus PPOB)")
    counter = fields.Char(string="Counter", default="1")

    def isi_pulsa(self):
        trx_id = self.env['sale.order'].get_active_name()
        same_trx = self.env['irs.trx'].search([('name', '=', self.product_code),('phone', '=', self.phone_number),('counter', '=', self.counter)], limit=1)
        if same_trx:
            delta = datetime.now()+timedelta(hours=7) - same_trx.trx_datetime
            if delta.seconds/3600 < 6:
                raise ValidationError('Transaksi serupa dengan counter: '+str(self.counter)+' sudah pernah dilakukan kurang dari 6 jam. ganti nilai counter jika ingin mengisi pulsa kembali. Transaksi terakhir: '+str(same_trx.trx_datetime))
            else:
                new = False
        else:
            new = True


        payload={}
        headers = {}
        insensitive_name = self.name.casefold()
        user = self.env['irs.info'].search([('insensitive_name', '=', insensitive_name)], limit=1).irs_username
        password = self.env['irs.info'].search([('insensitive_name', '=', insensitive_name)], limit=1).irs_password
        if password == False:
            raise ValidationError('ID IRS tidak dapat ditemukan di database odoo. Silakan cek apakah penulisan ID sudah benar.')
        
        produk_pulsa = self.env['product.product'].search([('default_code', '=', self.product_code)],limit=1).id
        if produk_pulsa == False:
            raise ValidationError('Tidak ada kode produk tersedia di database. Buat produk dengan kode internal: '+str(self.product_code))
        
        product_code = self.env['irs.product.code'].search([('input_code', '=', self.product_code)], limit=1).name
        if product_code == False:
            raise ValidationError('Tidak ada kode produk tersedia di database. Silakan cek apakah penulisan kode produk sudah benar')

        if self.trx_type == False:
            url = "http://103.119.55.59:8080/api/h2h?id="+str(self.name)+"&pin="+str(self.irs_pin)+"&user="+str(user)+"&pass="+str(password)+"&kodeproduk="+str(product_code)+"&tujuan="+str(self.phone_number)+"&counter="+str(self.counter)+"&idtrx="+str(trx_id)
        else:
            trx_type = self.trx_type
            url = "http://103.119.55.59:8080/api/h2h?id="+str(self.name)+"&pin="+str(self.irs_pin)+"&user="+str(user)+"&pass="+str(password)+"&kodeproduk="+str(product_code)+"&tujuan="+str(self.phone_number)+"&counter="+str(self.counter)+"&idtrx="+str(trx_id)+"&jenis="+str(trx_type)

        response = requests.request("GET", url, headers=headers, data=payload)

        json_data = json.loads(response.text)

        if json_data:
            if json_data['rc'] == '0068' or json_data['rc'] == '68' or json_data['rc'] == '0027' or json_data['rc'] == '1':

                if new == True:
                    self.env['irs.trx'].create({
                        'name' : self.product_code,
                        'phone' : self.phone_number,
                        'trx_datetime': datetime.now()+timedelta(hours=7),
                        'counter': self.counter
                        })
                else:
                    same_trx.write({
                        'trx_datetime': datetime.now()+timedelta(hours=7),
                        })

                phone = json_data['tujuan']
                if 'sn' in json_data:
                    sn = json_data['sn']
                else: 
                    sn = '-'
                code = self.product_code
                self.env['sale.order'].add_product_pulsa(phone, sn, code)
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'type': 'warning',
                        'message': (str(json_data['msg']) + ". ID Transaksi: " + str(json_data['reffid'])+" "+str(json_data)),
                        'sticky' : True
                    }
                }
            else:
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'type': 'warning',
                        'message': ("Pengisian gagal. " + str(json_data['msg']) + ". ID Transaksi: " + str(json_data['reffid'])+" "+str(json_data)),
                        'sticky' : True
                    }
                }