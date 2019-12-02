# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class curso2(models.Model):
    _name = 'openacademy.curso2' #IMPORTANTE é o nome da táboa
    _description = "Cursos da OpenAcademy"
    #_sql_constraints = [('datas', 'CHECK(data_inicio != data_fin)', 'A data de inicio non pode ser maior que a data fin')]
    _sql_constraints = [('nome unico', 'unique(name)', 'Non se pode repetir o nome'), ('datas', 'CHECK(data_inicio <= data_fin)', 'A data de inicio non pode ser maior que a data fin')]

    name = fields.Char( required=True, string="Título do Curso") #IMPORTANTE o campo ten que chamarse name
    descripcion = fields.Text(string="Descripción")
    moeda_id = fields.Many2one ('res.currency')
    orzamento = fields.Monetary ("Orzamento", 'moeda_id')
    #Non funciona orzamento_sempre_en_euros = fields.Monetary ("Orzamento", 1)# En euros directamente. O rexistro EUR en res.currency ten id=1
    responsable_id = fields.Many2one('res.users', ondelete='set null', index=True,string="Responsable")# index=True crea un índice
    sesion_ids = fields.One2many('openacademy.sesion2','curso_id','sesion2')# Os campos One2many Non se almacena na BD
    porcentaxe= fields.Integer(string="Porcentaxe %")
    valor= fields.Float(compute="_valor", store=True)# Campo Calculado podemos  almacenalo na BD ou non.
    data_inicio = fields.Datetime(string="Data Inicio",default=lambda self: fields.Datetime.now())
    data_fin = fields.Datetime(string="Data Fin",default=lambda self: fields.Datetime.now())

    @api.depends('porcentaxe','orzamento')
    def _valor(self):
        for rexistro in self:
            rexistro.valor = float(rexistro.porcentaxe)*float(rexistro.orzamento) / 100


    @api.constrains ('data_inicio','data_fin')
    def _valida_data(self):
        for rexistro in self:
            for linea in rexistro.sesion_ids:
                 if (rexistro.data_inicio > linea.data_sesion) or (rexistro.data_fin < linea.data_sesion):
                     raise ValidationError ("A DATA DA SESIÓN %s ten que estar entre '%s' e '%s'" % (
                    linea.name, rexistro.data_inicio, rexistro.data_fin))

