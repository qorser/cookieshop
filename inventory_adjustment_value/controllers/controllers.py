# -*- coding: utf-8 -*-
# from odoo import http


# class InventoryAdjustmentValue(http.Controller):
#     @http.route('/inventory_adjustment_value/inventory_adjustment_value', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventory_adjustment_value/inventory_adjustment_value/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventory_adjustment_value.listing', {
#             'root': '/inventory_adjustment_value/inventory_adjustment_value',
#             'objects': http.request.env['inventory_adjustment_value.inventory_adjustment_value'].search([]),
#         })

#     @http.route('/inventory_adjustment_value/inventory_adjustment_value/objects/<model("inventory_adjustment_value.inventory_adjustment_value"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventory_adjustment_value.object', {
#             'object': obj
#         })
