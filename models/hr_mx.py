# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class HrMxHistorialPuestoTrabajo(models.Model):
    _name = 'hr_mx.historial_puesto_trabajo'
    _rec_name = "puesto_id"

    puesto_id = fields.Many2one('hr.job','Puesto de trabajo')
    fecha_inicio = fields.Date('Fecha inicio')
    fecha_fin = fields.Date('Fecha Fin')
    empleado_id = fields.Many2one('hr.employee','Empleado')

class HrMxHistorialPuestoTrabajo(models.Model):
    _name = 'hr_mx.historial_salario'
    _description = "Historial de salario"

    salario = fields.Float('Salario mensual')
    salario_diario = fields.Float('Salario diario')
    fecha_inicio = fields.Date('Fecha inicio')
    fecha_fin = fields.Date('Fecha Fin')
    contrato_id = fields.Many2one('hr.contract','Contrato')

class HrMxHistorialRotacionTienda(models.Model):
    _name = "hr_mx.historial_rotacion_tienda"
    _description = "Historial rotacion en tiendas"

    tienda_id = fields.Many2one('pos.config','Tienda')
    fecha_inicio = fields.Date('Fecha inicio')
    fecha_fin = fields.Date('Fecha Fin')
    empleado_id = fields.Many2one('hr.employee','Empleado')

class ActaAdministrativa(models.Model):
    _name = "hr_mx.acta_administrativa"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Acta ActaAdministrativa'
    _order = 'id desc'

    name = fields.Char('Nombre', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    empleado_id = fields.Many2one('hr.employee','Emnpleado',tracking=True)
    descripcion = fields.Text('Descripción',tracking=True)
    fecha = fields.Date('Fecha',tracking=True)


    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            seq_date = None
            if 'company_id' in vals:
                vals['name'] = self.env['ir.sequence'].with_context(force_company=vals['company_id']).next_by_code(
                    'hr_mx.acta_administrativa', sequence_date=seq_date) or _('New')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code('hr_mx.acta_administrativa', sequence_date=seq_date) or _('New')

        result = super(ActaAdministrativa, self).create(vals)
        return result
