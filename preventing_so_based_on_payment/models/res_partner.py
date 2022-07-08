# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP


class res_partner(models.Model):
    _inherit = 'res.partner'

    is_restricted = fields.Boolean("Restricted")  
    count_unpaid = fields.Char(compute='_payment_total', string="Total Not Paid",
        groups='account.group_account_invoice,account.group_account_readonly')
    max_unpaid = fields.Char(string="Maximum Unpaid", default="2", help="Maximum unpaid invoices allowed for customers.")

    def _payment_total(self):
        print('HAHAHAH')
        print(self.max_unpaid)
        if not self.ids:
            return True

        all_partners_and_children = {}
        all_partner_ids = []
        for partner in self.filtered('id'):
            # price_total is in the company currency
            all_partners_and_children[partner] = self.with_context(active_test=False).search([('id', 'child_of', partner.id)]).ids
            all_partner_ids += all_partners_and_children[partner]


        domain = [
            ('partner_id', 'in', all_partner_ids),
            ('state', 'not in', ['draft', 'cancel']),
            ('payment_state', 'in', ['not_paid']),
            ('move_type', 'in', ('out_invoice', 'out_refund')),
        ]
        price_totals = self.env['account.move'].read_group(
                domain=domain,
                fields=['amount_total_signed'],
                groupby=['payment_state'],
            )

        print(price_totals)
        #SUDAH DAPAT HASILNYA. HASILNYA: JUMLAH IMVOICE PER PAYMENT STATUS (payment_state_count), DAN JUMLAH NOMINAL PER PAYMENT STATUS (amount_total_signed).
        if price_totals:
            self.count_unpaid=price_totals[0]['payment_state_count']
        else:
            self.count_unpaid=0