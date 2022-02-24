# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Employee(models.Model):
    _inherit = "hr.employee"

    area_id = fields.Many2one('hr.area',string='Area')
    # historial_puesto_ids = fields.One2many('hr_mx.historial_puesto_trabajo','empleado_id',string='Historial de puestos')
    historial_rotacion_tienda_ids = fields.One2many('hr_mx.historial_rotacion_tienda','empleado_id',string='Carrera Quemeniana',tracking=True)
    jornada = fields.Selection([
        ('diurno', 'Diurno'),
        ('nocturno', 'Nocturno'),
        ('mixto', 'Mixto')],'Jornada')

class hr_planilla(models.Model):
    _name = 'hr_mx.planilla'
    _description = "Planilla MX"
    _rec_name = 'nombre'

    nombre = fields.Char('Nombre planilla')
    salario = fields.Boolean('Incluir salario')
    # pago_planificado = fields.Selection([ ('bimensual', 'Bimensual'),('mensual', 'Mensual'),],'Pago planificado', default='bimensual')
    ingreso_ids = fields.One2many('hr_mx.planilla_ingreso','planilla_id','Ingresos')
    deduccion_ids = fields.One2many('hr_mx.planilla_deduccion','planilla_id','Deducciones')

class hr_planilla_ingreso(models.Model):
    _name = 'hr_mx.planilla_ingreso'
    _description = "Ingreso planilla mx"
    _rec_name = 'nombre'

    planilla_id = fields.Many2one('hr_mx.planilla','Planilla')
    nombre = fields.Char('Nombre')
    regla_ids = fields.Many2many('hr.salary.rule','hr_mx_ingreso_regla_rel',string='Reglas')
    sumar_total = fields.Boolean('Sumar en total')

class hr_planilla_deduccion(models.Model):
    _name = 'hr_mx.planilla_deduccion'
    _description = "Planilla deduccion MX"
    _rec_name = 'nombre'

    planilla_id = fields.Many2one('hr_mx.planilla','Planilla')
    nombre = fields.Char('Nombre')
    regla_ids = fields.Many2many('hr.salary.rule','hr_mx_deduccion_regla_rel',string='Reglas')

class Area(models.Model):
    _name = 'hr.area'
    _description = "HR Area"

    name = fields.Char('Nombre')
