# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrderLine(models.Model):
	_inherit = 'sale.order.line'

	price_status = fields.Char()

	@api.onchange('price_unit')
	def call_wizard(self):
		if self.price_unit < self.product_id.standard_price:
			self.price_status = 'under'
			return {
				'value':{},
				'warning':{
					'title':'Warning',
					'message':'Produk "'+self.product_id.name+'" dijual di bawah modal. Silakan perbaiki harga jual jika diperlukan!'
				}
			}
		else:
			self.price_status = 'upper'