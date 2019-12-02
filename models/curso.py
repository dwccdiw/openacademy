# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class openacademy(models.Model):
# _name = 'openacademy.openacademy'
#
# name = fields.Char()
# value = fields.Integer()
# value2 = fields.Float(compute="_value_pc", store=True)
# description = fields.Text()
#
# @api.depends('value')
# def _value_pc(self):
#      self.value2 = float(self.value) / 100
class curso(models.Model):
    _name = 'openacademy.curso' #IMPORTANTE é o nome da táboa
    _description = "Cursos da OpenAcademy"
    _sql_constraints = [('nome unico', 'unique(name)', 'Non se pode repetir o nome')]

    name = fields.Char( required=True, string="Título do Curso") #IMPORTANTE o campo ten que chamarse name
    descripcion = fields.Text(string="Descripción")
    moeda_id = fields.Many2one ('res.currency')
    orzamento = fields.Monetary ("Orzamento", 'moeda_id')
    responsable_id = fields.Many2one('res.users', ondelete='set null',  index=True,string="Responsable")

