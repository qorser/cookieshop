# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import fields, models
import json
from odoo.exceptions import UserError, ValidationError
import requests

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

    def isi_pulsa(self):
        trx_id = self.env['sale.order'].get_active_name()
        # trx_id = "0"+str(trx_id)

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
            url = "http://103.119.55.59:8080/api/h2h?id="+str(self.name)+"&pin="+str(self.irs_pin)+"&user="+str(user)+"&pass="+str(password)+"&kodeproduk="+str(product_code)+"&tujuan="+str(self.phone_number)+"&counter=2&idtrx="+str(trx_id)
        else:
            trx_type = self.trx_type
            url = "http://103.119.55.59:8080/api/h2h?id="+str(self.name)+"&pin="+str(self.irs_pin)+"&user="+str(user)+"&pass="+str(password)+"&kodeproduk="+str(product_code)+"&tujuan="+str(self.phone_number)+"&counter=2&idtrx="+str(trx_id)+"&jenis="+str(trx_type)

        response = requests.request("GET", url, headers=headers, data=payload)

        json_data = json.loads(response.text)

        if json_data:
            if json_data['success'] == False:
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'type': 'warning',
                        'message': ("Pengisian gagal. " + str(json_data['msg']) + ". ID Transaksi: " + str(json_data['reffid'])),
                        'sticky' : True
                    }
                }
            else:
                phone = json_data['tujuan']
                sn = json_data['sn']
                code = self.product_code
                self.env['sale.order'].add_product_pulsa(phone, sn, code)
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'type': 'warning',
                        'message': (str(json_data['msg']) + ". ID Transaksi: " + str(json_data['reffid'])),
                        'sticky' : True
                    }
                }
