# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, ValidationError

class StockInventoryAdjustmentName(models.TransientModel):
    _inherit= 'stock.inventory.adjustment.name'
    
    user_id = fields.Many2one(
        'res.users', string='Responsible', default=lambda self: self.env.user, required=True)

    def action_apply(self):
        return self.quant_ids.with_context(
            inventory_name=self.inventory_adjustment_name, user_id=self.user_id).action_apply_inventory()