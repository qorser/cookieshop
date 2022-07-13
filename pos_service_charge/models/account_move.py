# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

#QORSER ADDITION
class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.constrains('l10n_id_kode_transaksi', 'line_ids')
    def _constraint_kode_ppn(self):
        ppn_tag = self.env.ref('l10n_id.ppn_tag')
        for move in self.filtered(lambda m: m.l10n_id_kode_transaksi != '08'):

            if any(ppn_tag.id in line.tax_tag_ids.ids for line in move.line_ids if line.exclude_from_invoice_tab is False and not line.display_type) \
                    and any(ppn_tag.id not in line.tax_tag_ids.ids for line in move.line_ids if line.exclude_from_invoice_tab is False and not line.display_type):
                for move_line in move.invoice_line_ids:
                    pos_id = 1
                    service_product_id = self.env['pos.config'].search([('id', '=', pos_id)], limit=1).product_id.id

                    if move_line.product_id.id == service_product_id:
                        move_line.write({
                            'tax_tag_ids' : [9],
                            })
            if any(ppn_tag.id in line.tax_tag_ids.ids for line in move.line_ids if line.exclude_from_invoice_tab is False and not line.display_type) \
                    and any(ppn_tag.id not in line.tax_tag_ids.ids for line in move.line_ids if line.exclude_from_invoice_tab is False and not line.display_type):        
                raise UserError(_('Cannot mix VAT subject and Non-VAT subject items in the same invoice with this kode transaksi.'))
        
        for move in self.filtered(lambda m: m.l10n_id_kode_transaksi == '08'):
            if any(ppn_tag.id in line.tax_tag_ids.ids for line in move.line_ids if line.exclude_from_invoice_tab is False and not line.display_type):
                raise UserError('Kode transaksi 08 is only for non VAT subject items.')