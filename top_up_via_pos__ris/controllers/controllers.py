# -*- coding: utf-8 -*-
from odoo import http
import requests


class TopUpViaPosRis(http.Controller):

    @http.route('/isipulsa', type='json', auth='public')
    def isipulsa(self, phone, id, pin, user, password, kode, trx_id):
        print('HALO INI CONTROLLER')      
        print(phone) 
        payload={}
        headers = {}
        url = "http://103.119.55.59:8080/api/h2h?id="+str(id)+"&pin="+str(pin)+"&user="+str(user)+"&pass="+str(password)+"&kodeproduk="+str(kode)+"&tujuan=08997927000&counter=1&idtrx="+str(trx_id)
        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

        # return "Berhasil diisi"
        return response.text








