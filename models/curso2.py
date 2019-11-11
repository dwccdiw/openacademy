# -*- coding: utf-8 -*-

from odoo import models, fields, api


class curso2(models.Model):
    _name = 'openacademy.curso2' #IMPORTANTE é o nome da táboa
    _description = "Cursos da OpenAcademy"

    name = fields.Char( required=True, string="Título do Curso") #IMPORTANTE o campo ten que chamarse name
    descripcion = fields.Text(string="Descripción")
    moeda_id = fields.Many2one ('res.currency')
    orzamento = fields.Monetary ("Orzamento", 'moeda_id')
    #Non funciona orzamento_sempre_en_euros = fields.Monetary ("Orzamento", 1)# En euros directamente. O rexistro EUR en res.currency ten id=1
    responsable_id = fields.Many2one('res.users', ondelete='set null', index=True,string="Responsable")# index=True crea un índice
    sesion_ids = fields.One2many('openacademy.sesion2','curso_id','sesion2')# Os campos One2many Non se almacena na BD
    _sql_constraints = [('nome unico', 'unique(name)', 'Non se pode repetir o nome')]
    porcentaxe= fields.Integer(string="Porcentaxe %")
    valor= fields.Float(compute="_valor", store=True)# Campo Calculado podemos  almacenalo na BD ou non.


    @api.depends('porcentaxe')
    def _valor(self):
        for rexistro in self:
            rexistro.valor = float(rexistro.porcentaxe)*float(rexistro.orzamento) / 100
