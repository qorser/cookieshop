# -*- coding: utf-8 -*-
from odoo import http
import requests


class TopUpViaPosRis(http.Controller):
#     @http.route('/top_up_via_pos__ris/top_up_via_pos__ris', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/top_up_via_pos__ris/top_up_via_pos__ris/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('top_up_via_pos__ris.listing', {
#             'root': '/top_up_via_pos__ris/top_up_via_pos__ris',
#             'objects': http.request.env['top_up_via_pos__ris.top_up_via_pos__ris'].search([]),
#         })

#     @http.route('/top_up_via_pos__ris/top_up_via_pos__ris/objects/<model("top_up_via_pos__ris.top_up_via_pos__ris"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('top_up_via_pos__ris.object', {
#             'object': obj
#         })

    @http.route('/isipulsa', type='json', auth='public')
    def isipulsa(self, phone, id, pin, user, password):
        print('HALO INI CONTROLLER')      
        print(phone) 
        payload={}
        headers = {}
        url = "http://103.119.55.59:8080/api/h2h?id="+str(id)+"&pin="+str(pin)+"&user="+str(user)+"&pass="+str(password)+"&kodeproduk=T1&tujuan=08997927000&counter=1&idtrx=240622-1"
        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

        # return "Berhasil diisi"
        return response.text








