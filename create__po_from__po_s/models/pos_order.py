# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class PosOrder(models.Model):
    _inherit = "pos.order"

    @api.model
    def create_from_ui(self, orders, draft=False):
        order_ids = []

        for order in orders:
            partners=[]
            lines = order['data']['lines']
            for line in lines:
                product = self.env['product.product'].search([('id', '=', line[2]['product_id'])], limit=1)
                create_PO =  product.create_PO_from_PoS
                if create_PO == True:
                    if product.variant_seller_ids.id == False:
                        raise ValidationError("Vendor list is empty!! Please set vendor list on product form on backend!")
                    else:
                        partner_id = product.variant_seller_ids[0].name.id
                        if partners:
                            i=0
                            for partner in partners:
                                if partner["id"] == partner_id:
                                    i = i+1
                                    po_id = self.env['purchase.order'].search([('id', '=', partner["po_id"])], limit=1)
                                    order_line = []
                                    order_line.append((0,0,
                                        {'product_id' : line[2]['product_id'],  
                                        'product_qty' : line[2]['qty'],
                                        'price_unit' : line[2]['price_unit'],
                                        'taxes_id' : line[2]['tax_ids']
                                        }))
                                    po_id.write(
                                       {'order_line' : order_line})
                            
                            if i == 0:                        
                                order_line = []
                                order_line.append( (0,0,
                                    {'product_id' : line[2]['product_id'],  
                                    'product_qty' : line[2]['qty'],
                                    'price_unit' : line[2]['price_unit'],
                                    'taxes_id' : line[2]['tax_ids']
                                    })
                                )
                                self.env['purchase.order'].create({
                                    'partner_id' : partner_id,
                                    'order_line' :order_line
                                })
                                
                                partners.append({
                                    'id' : partner_id,
                                    'po_id' : po_id.id
                                    })
                        else:
                            order_line = []
                            order_line.append( (0,0,
                                {'product_id' : line[2]['product_id'],  
                                'product_qty' : line[2]['qty'],
                                'price_unit' : line[2]['price_unit'],
                                'taxes_id' : line[2]['tax_ids']
                                })
                            )
                            po_id = self.env['purchase.order'].create({
                                'partner_id' : partner_id,
                                'order_line' : order_line
                            })
                            
                            partners.append({
                                'id' : partner_id,
                                'po_id' : po_id.id
                                })

            existing_order = False
            if 'server_id' in order['data']:
                existing_order = self.env['pos.order'].search(['|', ('id', '=', order['data']['server_id']), ('pos_reference', '=', order['data']['name'])], limit=1)
            if (existing_order and existing_order.state == 'draft') or not existing_order:
                order_ids.append(self._process_order(order, draft, existing_order))

        return self.env['pos.order'].search_read(domain = [('id', 'in', order_ids)], fields = ['id', 'pos_reference'])