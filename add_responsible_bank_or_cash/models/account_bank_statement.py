# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountBankStatement(models.Model):
    _inherit = "account.bank.statement"
    
    user_id = fields.Many2one(
        'res.users', string='Responsible', default=lambda self: self.env.user, required=True)