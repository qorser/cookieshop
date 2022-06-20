# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    PO_origin = fields.Many2one('pos.order', compute='_PO_origin')

    def _PO_origin(self):
        if self.origin:
            if "Order" in str(self.origin):
                pos_order_id = self.env["pos.order"].search([('pos_reference', '=', self.origin)], limit=1).id
                self.PO_origin = pos_order_id
            else:
                self.PO_origin = False
        else:
            self.PO_origin = False

    