# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero

class StockQuant(models.Model):
	_inherit = 'stock.quant'

	def _get_inventory_move_values(self, qty, location_id, location_dest_id, out=False):
		self.ensure_one()
		if fields.Float.is_zero(qty, 0, precision_rounding=self.product_uom_id.rounding):
			name = 'Product Quantity Confirmed'
		else:
			name = 'Product Quantity Updated'
		print(self.env.context)
		return {
			'name': self.env.context.get('inventory_name') or name,
			'user_id': (self.env.context.get('user_id')).id,
			'product_id': self.product_id.id,
			'product_uom': self.product_uom_id.id,
			'product_uom_qty': qty,
			'company_id': self.company_id.id or self.env.company.id,
			'state': 'confirmed',
			'location_id': location_id.id,
			'location_dest_id': location_dest_id.id,
			'is_inventory': True,
			'move_line_ids': [(0, 0, {
				'product_id': self.product_id.id,
				'product_uom_id': self.product_uom_id.id,
				'qty_done': qty,
				'location_id': location_id.id,
				'location_dest_id': location_dest_id.id,
				'company_id': self.company_id.id or self.env.company.id,
				'lot_id': self.lot_id.id,
				'package_id': out and self.package_id.id or False,
				'result_package_id': (not out) and self.package_id.id or False,
				'owner_id': self.owner_id.id,
			})]
			}

	def _apply_inventory(self):
		move_vals = []
		diference = []
		if not self.user_has_groups('stock.group_stock_manager'):
			raise UserError(_('Only a stock manager can validate an inventory adjustment.'))
		for quant in self:
			diference.append(quant.inventory_diff_quantity)
			# Create and validate a move so that the quant matches its `inventory_quantity`.
			if float_compare(quant.inventory_diff_quantity, 0, precision_rounding=quant.product_uom_id.rounding) > 0:
				move_vals.append(
				    quant._get_inventory_move_values(quant.inventory_diff_quantity,
				                                     quant.product_id.with_company(quant.company_id).property_stock_inventory,
				                                     quant.location_id))
			else:
				move_vals.append(
				    quant._get_inventory_move_values(-quant.inventory_diff_quantity,
				                                     quant.location_id,
				                                     quant.product_id.with_company(quant.company_id).property_stock_inventory,
			                                         out=True))

		print('HAHAHHA')
		print(move_vals)
		moves = self.env['stock.move'].with_context(inventory_mode=False).create(move_vals)		
		moves._action_done()

		total_cost = 0
		i=0
		for move in moves:
			cost = move.product_id.standard_price * diference[i]
			total_cost = total_cost + cost
			move.write({
				'diference' : diference[i],
				})
			i=i+1

		report = self.env['stock.quant.report'].create({
			'name' : moves[0]['reference'],
			'date' : moves[0]['date'],
			'user_id' : move_vals[0]['user_id'],
			'product_adjusted' : len(moves),
			'total_cost_adjusted' : total_cost
			})

		for move in moves:
			move.write({
				'report_id' : report.id
				})
			i=i+1


		self.location_id.write({'last_inventory_date': fields.Date.today()})
		date_by_location = {loc: loc._get_next_inventory_date() for loc in self.mapped('location_id')}
		for quant in self:
			quant.inventory_date = date_by_location[quant.location_id]
		self.write({'inventory_quantity': 0, 'user_id': False})
		self.write({'inventory_diff_quantity': 0})