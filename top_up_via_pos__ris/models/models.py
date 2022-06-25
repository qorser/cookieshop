# -*- coding: utf-8 -*-

from odoo import models, fields, api


class top_up_via_pos__ris(models.Model):
    _name = 'top_up_via_pos__ris.top_up_via_pos__ris'
    _description = 'top_up_via_pos__ris.top_up_via_pos__ris'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    def print(self):
        print("HELLO BUDDY")
        # return("hello")
        return { 
            'type': 'ir.actions.act_url',
            'url': '/isipulsa',
            'target': 'self',
            'res_id': self.id,
        }