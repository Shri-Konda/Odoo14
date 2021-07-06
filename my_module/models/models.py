# -*- coding: utf-8 -*-

from odoo import models, fields

class my_module(models.Model):
    _name = 'my_module.my_module'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float()
    description = fields.Text()