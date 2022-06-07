# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero

class StockMove(models.Model):
    _inherit = "stock.move"

    report_id = fields.Char()
    total_cost = fields.Char(String="Total Cost", compute="_compute_total_cost")

    diference = fields.Char(String="Diference")
    responsible = fields.Many2one('res.partner', 'Responsible')

    @api.depends('diference','product_id')
    def _compute_total_cost(self):
        for adjustment_line in self:
            diference = adjustment_line.diference
            if adjustment_line.diference == False:
                diference = 0
            adjustment_line.total_cost = float(adjustment_line.product_id.standard_price) * float(diference)
            