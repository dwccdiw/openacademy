# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class curso3(models.Model):
    _name = 'openacademy.curso3' #IMPORTANTE é o nome da táboa
    _description = "Cursos da OpenAcademy 3"
    _sql_constraints = [('nome unico', 'unique(name)', 'Non se pode repetir o nome'), ('datas', 'CHECK(data_inicio <= data_fin)', 'A data de inicio non pode ser maior que a data fin')]

    name = fields.Char( compute="_inicio_titulo",store=True) #IMPORTANTE o campo ten que chamarse name
    titulo = fields.Char( required=True, string="Título do Curso")
    descripcion = fields.Text(string="Descripción")
    cartel = fields.Binary (string='Cartel')
    moeda_euro_id = fields.Many2one ('res.currency',default=lambda self: self.env['res.currency'].search([('name', '=', "EUR")], limit=1))
    material_en_euros = fields.Monetary ("Gasto en material", 'moeda_euro_id')
    docencia_en_euros = fields.Monetary ("Gasto en docencia", 'moeda_euro_id')
    orzamento_total = fields.Monetary("Gasto total", 'moeda_euro_id', compute="_orzamento", store=True)
    relator1_id = fields.Many2one('res.partner', ondelete='set null', index=True,string="Relator 1")# index=True crea un índice
    relator2_id = fields.Many2one ('res.partner', ondelete='set null', index=True, string="Relator 2")  # index=True crea un índice
    sesion_ids = fields.One2many('openacademy.sesion3','curso_id','sesion3')# Os campos One2many Non se almacena na BD
    data_inicio = fields.Datetime (string="Data Inicio", required=True, default=lambda self: fields.Datetime.now ())
    data_fin = fields.Datetime (string="Data Fin", required=True, default=lambda self: fields.Datetime.now ())
    autorizado = fields.Boolean (string="¿Autorizado?", default=True)

    @api.depends('docencia_en_euros','material_en_euros')
    def _orzamento(self):
        for rexistro in self:
            rexistro.orzamento_total = float(rexistro.material_en_euros) + float(rexistro.docencia_en_euros)

    @api.constrains ('data_inicio','data_fin')
    def _valida_data(self):
        for rexistro in self:
            for linea in rexistro.sesion_ids:
                 if (rexistro.data_inicio > linea.data_sesion) or (rexistro.data_fin < linea.data_sesion):
                     raise ValidationError ("A DATA DA SESIÓN %s ten que estar entre '%s' e '%s'" % (
                    linea.name, rexistro.data_inicio, rexistro.data_fin))

    @api.depends ('titulo', 'data_inicio')
    def _inicio_titulo(self):
        for rexistro in self:
            if rexistro.titulo  and rexistro.data_inicio:
                rexistro.name = rexistro.data_inicio.strftime ("%d/%m/%Y") + "-" + str(rexistro.titulo)
            else:
                rexistro.name = fields.Date.today ().strftime ("%d/%m/%Y") + " noname"