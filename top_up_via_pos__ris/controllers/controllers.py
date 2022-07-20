# -*- coding: utf-8 -*-
from odoo import http
import requests
import json
from odoo.exceptions import UserError, ValidationError


class TopUpViaPosRis(http.Controller):

    @http.route('/isipulsa', type='json', auth='public')
    def isipulsa(self, phone, id, pin, kode, trx_id, trx_type):
        payload={}
        headers = {}
        insensitive_name = id.casefold()
        user = http.request.env['irs.info'].search([('insensitive_name', '=', insensitive_name)], limit=1).irs_username
        password = http.request.env['irs.info'].search([('insensitive_name', '=', insensitive_name)], limit=1).irs_password
        if password == False:
            return 'ID IRS tidak dapat ditemukan di database odoo. Silakan cek apakah penulisan ID sudah benar.'
        product_code = http.request.env['irs.product.code'].search([('input_code', '=', kode)], limit=1).name
        if product_code == False:
            return 'Tidak ada kode produk tersedia di database. Silakan cek apakah penulisan kode produk sudah benar'
        else:
            produk_pulsa = http.request.env['product.product'].search([('default_code', '=', kode)],limit=1).id
            if produk_pulsa == False:
                return 'Tidak ada kode produk tersedia di database. Buat produk dengan kode internal: '+str(kode)

        if len(trx_type) > 0:
            url = "http://103.119.55.59:8080/api/h2h?id="+str(id)+"&pin="+str(pin)+"&user="+str(user)+"&pass="+str(password)+"&kodeproduk="+str(product_code)+"&tujuan="+str(phone)+"&counter=3&idtrx="+str(trx_id)+"&jenis="+str(trx_type)
        else:
            url = "http://103.119.55.59:8080/api/h2h?id="+str(id)+"&pin="+str(pin)+"&user="+str(user)+"&pass="+str(password)+"&kodeproduk="+str(product_code)+"&tujuan="+str(phone)+"&counter=3&idtrx="+str(trx_id)

        print(url)

        response = requests.request("GET", url, headers=headers, data=payload)

        json_data = json.loads(response.text)

        return json_data






