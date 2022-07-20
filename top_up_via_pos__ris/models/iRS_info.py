# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class IrsInfo(models.Model):
    _name = 'irs.info'
    _description = 'iRS Account ID, PIN and More Information'

    name = fields.Char(String="IRS ID")
    insensitive_name = fields.Char(compute='compute_insensitive_name', store=True)
    irs_username = fields.Char(String="IRS Username")
    irs_password = fields.Char(String="IRS Password")

    @api.depends('name')
    def compute_insensitive_name(self):
        for record in self:
            record.insensitive_name = record.name.casefold()


    