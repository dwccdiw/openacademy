# -*- coding: utf-8 -*-

from odoo import models, fields, api


class curso2(models.Model):
    _name = 'openacademy.curso2' #IMPORTANTE é o nome da táboa
    _description = "Cursos da OpenAcademy"

    name = fields.Char( required=True, string="Título do Curso") #IMPORTANTE o campo ten que chamarse name
    descripcion = fields.Text(string="Descripción")
    moeda_id = fields.Many2one ('res.currency')
    orzamento = fields.Monetary ("Orzamento", 'moeda_id')
    responsable_id = fields.Many2one('res.users', ondelete='set null',  index=True,string="Responsable")
    sesion_ids = fields.One2many('openacademy.sesion',curso_id,'sesions')
    _sql_constraints = [('nome unico', 'unique(nome_curso)', 'Non se pode repetir o nome')]
