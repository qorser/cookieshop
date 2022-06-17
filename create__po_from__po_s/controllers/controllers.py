# -*- coding: utf-8 -*-
# from odoo import http


# class CreatePoFromPoS(http.Controller):
#     @http.route('/create__po_from__po_s/create__po_from__po_s', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/create__po_from__po_s/create__po_from__po_s/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('create__po_from__po_s.listing', {
#             'root': '/create__po_from__po_s/create__po_from__po_s',
#             'objects': http.request.env['create__po_from__po_s.create__po_from__po_s'].search([]),
#         })

#     @http.route('/create__po_from__po_s/create__po_from__po_s/objects/<model("create__po_from__po_s.create__po_from__po_s"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('create__po_from__po_s.object', {
#             'object': obj
#         })
