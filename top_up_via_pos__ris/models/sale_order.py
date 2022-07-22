# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.osv import expression
from odoo.tools import float_is_zero, html_keep_url, is_html_empty

from odoo.addons.payment import utils as payment_utils

class SaleOrder(models.Model):
    _inherit = "sale.order"

    jumlah_pulsa = fields.Char()
   
    def action_topup(self):
        view = self.env.ref('top_up_via_pos__ris.isi_pulsa_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        return {
            'name': 'Isi Pulsa',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'isi.pulsa.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': context,
        }

    def get_active_name(self):
        so_id = self.env.context.get('active_id')
        SO = self.search([('id', '=', so_id)], limit=1)
        name = SO.name
        pulsa = SO.jumlah_pulsa
        if pulsa == False:
            jumlah_pulsa = 1
        else:
           jumlah_pulsa = int(pulsa) + 1
        name = str(name)+"("+str(jumlah_pulsa)+")"
        return name

    def add_product_pulsa(self, phone, sn, code):
        so_id = self.env.context.get('active_id')
        produk_pulsa = self.env['product.product'].search([('default_code', '=', code)],limit=1).id
        lines_vals = [
            (0, 0, {
                'product_id': produk_pulsa,
                'product_uom_qty': 1,
                'name': "Nomor tujuan: "+str(phone)+", SN: "+str(sn)
            })]

        SO = self.search([('id', '=', so_id)], limit=1)
        pulsa = SO.jumlah_pulsa
        if pulsa == False:
            jumlah_pulsa = 1
        else:
            jumlah_pulsa = int(pulsa) + 1
        SO.write({
            'order_line': lines_vals,
            'jumlah_pulsa': jumlah_pulsa
        })