# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero

class StockQuantReport(models.Model):
	_name = "stock.quant.report"

	name = fields.Char()
	product_adjusted = fields.Char(String="Product Adjusted")

	company_id = fields.Many2one('res.company', 'Company', required=True, default=lambda self: self.env.company)
	currency_id = fields.Many2one('res.currency', related='company_id.currency_id', readonly=True)

	total_cost_adjusted = fields.Char(String="Total Cost Adjusted", currency_field="currency_id",)
	date = fields.Datetime('Date', default=fields.Datetime.now, required=True)
	responsible = fields.Many2one('res.partner', 'Responsible')

	def action_view_inventory_adjustments(self):
		self.ensure_one()
		action = self.env["ir.actions.actions"]._for_xml_id("stock.stock_move_action")
		action['domain'] = [
		    ('report_id', '=', self.id),
		]
		return action

	def _get_currency(self):
		self.currency_id = self.env.ref('base.main_company').currency_id