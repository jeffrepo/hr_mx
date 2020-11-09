# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    def compute_sheet(self):
        for nomina in self:
            entradas = False
            if nomina.employee_id.contract_id.structure_type_id and  nomina.employee_id.contract_id.structure_type_id.default_struct_id:
                if  nomina.employee_id.contract_id.structure_type_id.default_struct_id.input_line_type_ids:
                    entradas = [entrada for entrada in  nomina.employee_id.contract_id.structure_type_id.default_struct_id.input_line_type_ids]
            if entradas:
                if len(nomina.input_line_ids) == 0:
                    for entrada in entradas:
                        entrada_id = self.env['hr.payslip.input'].create({'payslip_id': nomina.id,'input_type_id': entrada.id})
        res =  super(HrPayslip, self).compute_sheet()
        return res


    def _get_worked_day_lines(self):
        res = super(HrPayslip, self)._get_worked_day_lines()
        tipos_ausencias_ids = self.env['hr.leave.type'].search([])

        horas = 0
        dias = 0
        for linea in res:
            tipo_id = self.env['hr.work.entry.type'].search([('id','=',linea['work_entry_type_id'])])
            if tipo_id and tipo_id.is_leave and tipo_id.descontar_nomina == False:
                horas += linea['number_of_hours']
                dias += linea['number_of_days']


        datos = {'dias':dias, 'horas': horas}
        ausencias_restar = []
        dias_ausentados_restar = 0
        if self.employee_id.contract_id:
            contracts = self.employee_id.contract_id

        for ausencia in tipos_ausencias_ids:
            if ausencia.work_entry_type_id and ausencia.work_entry_type_id.descontar_nomina:
                ausencias_restar.append(ausencia.work_entry_type_id.id)

        for r in res:
            type_id = self.env['hr.work.entry.type'].search([('id','=',r['work_entry_type_id'])])
            if type_id and type_id.is_leave == False:
                r['number_of_hours'] += horas
                r['number_of_days'] += dias

            trabajo_id = self.env['hr.work.entry.type'].search([('code','=','WORK100')])
            if len(ausencias_restar)>0:
                if r['work_entry_type_id'] in ausencias_restar:
                    dias_ausentados_restar += r['number_of_days']

        return res
