# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.template'

    create_PO_from_PoS = fields.Boolean()
