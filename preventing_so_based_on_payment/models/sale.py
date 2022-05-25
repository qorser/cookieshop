# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, ValidationError

class SaleOrder(models.Model):
	_inherit = "sale.order"

	def action_confirm(self):
		# super().action_confirm(values)
		super(SaleOrder, self).action_confirm()
		if self.partner_id.is_restricted == True and int(self.partner_id.count_unpaid) > int(self.partner_id.max_unpaid) and self.partner_id.max_unpaid != False:
			# raise UserError('SO creation cannot be done because the unpaid invoices has reached the limit. Please make payment in advance.')
			raise UserError('Pembuatan SO tidak dapat dilakukan karena invoice yang belum dibayar mencapai limit. Silakan lakukan pembayaran terlebih dahulu.')

