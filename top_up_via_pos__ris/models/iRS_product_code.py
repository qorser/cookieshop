# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class IrsProductCode(models.Model):
    _name = 'irs.product.code'
    _description = 'Conversion of Inputed Code to iRS Product Code'

    name = fields.Char(String="iRS Code")
    input_code = fields.Char(String="Product Input Code")

    