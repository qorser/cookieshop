# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    POS_origin = fields.Many2one('pos.order', compute='_POS_origin')

    def _POS_origin(self):
        if self.origin:
            if "Order" in str(self.origin):
                pos_order_id = self.env["pos.order"].search([('pos_reference', '=', self.origin)], limit=1).id
                self.POS_origin = pos_order_id
            else:
                self.POS_origin = False
        else:
            self.POS_origin = False

    