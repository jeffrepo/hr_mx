# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _

class Contract(models.Model):
    _inherit = 'hr.contract'

    historial_salario_ids = fields.One2many('hr_mx.historial_salario','contrato_id',string='Historial de salario')
