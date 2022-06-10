# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    loyalty_id = fields.Many2one(related='company_id.loyalty_id', string='Loyalty Program', domain="[('company_id', '=', company_id)]", readonly=False, help='Set Loyalty Program on Sale Order')
