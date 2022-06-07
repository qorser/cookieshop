# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, ValidationError

class StockInventoryAdjustmentName(models.TransientModel):
    _inherit= 'stock.inventory.adjustment.name'
    
    responsible = fields.Many2one('res.partner', 'Responsible', required=True)

    def action_apply(self):
        return self.quant_ids.with_context(
            inventory_name=self.inventory_adjustment_name, responsible=self.responsible).action_apply_inventory()