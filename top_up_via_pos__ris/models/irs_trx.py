# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class IrsInfo(models.Model):
    _name = 'irs.trx'
    _description = 'iRS transaction'

    name = fields.Char(String="Produk")
    phone = fields.Char(String="Phone Number")
    trx_datetime = fields.Datetime(String="Transaction Date")
    counter = fields.Char(String = "Counter")


    