# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class create__po_from__po_s(models.Model):
#     _name = 'create__po_from__po_s.create__po_from__po_s'
#     _description = 'create__po_from__po_s.create__po_from__po_s'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
