# -*- coding: utf-8 -*-
# from odoo import http


# class PreventingSoBasedOnPayment(http.Controller):
#     @http.route('/preventing_so_based_on_payment/preventing_so_based_on_payment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/preventing_so_based_on_payment/preventing_so_based_on_payment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('preventing_so_based_on_payment.listing', {
#             'root': '/preventing_so_based_on_payment/preventing_so_based_on_payment',
#             'objects': http.request.env['preventing_so_based_on_payment.preventing_so_based_on_payment'].search([]),
#         })

#     @http.route('/preventing_so_based_on_payment/preventing_so_based_on_payment/objects/<model("preventing_so_based_on_payment.preventing_so_based_on_payment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('preventing_so_based_on_payment.object', {
#             'object': obj
#         })
