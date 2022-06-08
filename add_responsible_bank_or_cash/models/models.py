# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class add_responsible_bank_or_cash(models.Model):
#     _name = 'add_responsible_bank_or_cash.add_responsible_bank_or_cash'
#     _description = 'add_responsible_bank_or_cash.add_responsible_bank_or_cash'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
