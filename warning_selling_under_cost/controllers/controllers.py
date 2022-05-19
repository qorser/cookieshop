# -*- coding: utf-8 -*-
# from odoo import http


# class WarningSellingUnderCost(http.Controller):
#     @http.route('/warning_selling_under_cost/warning_selling_under_cost', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/warning_selling_under_cost/warning_selling_under_cost/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('warning_selling_under_cost.listing', {
#             'root': '/warning_selling_under_cost/warning_selling_under_cost',
#             'objects': http.request.env['warning_selling_under_cost.warning_selling_under_cost'].search([]),
#         })

#     @http.route('/warning_selling_under_cost/warning_selling_under_cost/objects/<model("warning_selling_under_cost.warning_selling_under_cost"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('warning_selling_under_cost.object', {
#             'object': obj
#         })
