# -*- coding: utf-8 -*-
# from odoo import http


# class AddResponsibleBankOrCash(http.Controller):
#     @http.route('/add_responsible_bank_or_cash/add_responsible_bank_or_cash', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add_responsible_bank_or_cash/add_responsible_bank_or_cash/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('add_responsible_bank_or_cash.listing', {
#             'root': '/add_responsible_bank_or_cash/add_responsible_bank_or_cash',
#             'objects': http.request.env['add_responsible_bank_or_cash.add_responsible_bank_or_cash'].search([]),
#         })

#     @http.route('/add_responsible_bank_or_cash/add_responsible_bank_or_cash/objects/<model("add_responsible_bank_or_cash.add_responsible_bank_or_cash"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add_responsible_bank_or_cash.object', {
#             'object': obj
#         })
