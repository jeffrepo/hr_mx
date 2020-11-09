# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    def compute_sheet(self):
        for nomina in self:
            entradas = False
            if contrato_id.structure_type_id and contrato_id.structure_type_id.default_struct_id:
                if contrato_id.structure_type_id.default_struct_id.input_line_type_ids:
                    entradas = [entrada for entrada in contrato_id.structure_type_id.default_struct_id.input_line_type_ids]
            if entradas:
                for entrada in entradas:
                    entrada_id = self.env['hr.payslip.input'].create({'payslip_id': nomina.id,'input_type_id': entrada.id})
        res =  super(HrPayslip, self).compute_sheet()
        return res
