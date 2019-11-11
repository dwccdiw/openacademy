# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import Warning
from odoo.exceptions import ValidationError


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

class sesion(models.Model):
    _name = 'openacademy.sesion' #IMPORTANTE é o nome da táboa
    _description = "Sesións dos cursos OpenAcademy "

    name = fields.Char (required=True, string="Nome da Sesión") #IMPORTANTE o campo ten que chamarse name
    data_sesion = fields.Datetime(string="Data da Sesión",default=lambda self: fields.Datetime.now())
    duracion = fields.Float(digits=(6, 2), string="Duración en horas", default=2)
    asentos = fields.Integer(string="Número de Asentos" )
    instructor_id = fields.Many2one('res.partner',string="Docente")
    nacionalidade = fields.Many2one ('res.country', string='Nacionalidade')
    foto = fields.Binary(string='Foto')
    sexo = fields.Selection([('male', 'Home'), ('female', 'Muller'), ('others', 'Outros')], string='Sexo')
    autorizado = fields.Boolean(string="¿Autorizado?", default=True)
    curso_id = fields.Many2one('openacademy.curso', ondelete='cascade', required=True,string="Título do Curso")
    # attendee_ids = fields.Many2many('res.partner',  string="Axudantes")
    # attendee_ids = fields.Many2many ('management.student', relation='your_table_name', column1='course_id',
    #                                  column2='student_id', string="Attendees")
    axudantes_ids = fields.Many2many('res.partner', ondelete='set null',string="Axudantes" )
    moeda_id = fields.Many2one ('res.currency')
    custo_por_hora = fields.Monetary ("Custo por hora", 'moeda_id')

    @api.multi
    def button_check_duracion(self): # é necesario engadir no xml da vista no header o botón
        self.ensure_one ()
        for sesion in self:
            if self.duracion < 1 or self.duracion > 4:
                raise Warning (
                    'A duración da %s ten que ser entre 1 e 4 horas' % sesion.name)
            else:
                raise Warning (
                    'Duración da %s correcta' % sesion.name)
                return True

    @api.constrains ('duracion')
    def _constrain_duracion_sesion(self):
        for sesion in self:
            if self.duracion < 1 or self.duracion > 4:
                raise ValidationError (
                    'A duración da %s ten que ser entre 1 e 4 horas' % sesion.name)
