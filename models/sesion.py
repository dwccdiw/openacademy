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

class sesion(models.Model):
    _name = 'openacademy.sesion' #IMPORTANTE é o nome da táboa
    _description = "Sesións dos cursos OpenAcademy "

    name = fields.Char (required=True, string="Nome da Sesión") #IMPORTANTE o campo ten que chamarse name
    data_sesion = fields.Date(string="Data da Sesión")
    duracion = fields.Float(digits=(6, 2), string="Duración en horas")
    asentos = fields.Integer(string="Número de asentos")
    instructor_id = fields.Many2one('res.partner',string="Docente")
    curso_id = fields.Many2one('openacademy.curso', ondelete='cascade', required=True,string="Título do Curso")
    # attendee_ids = fields.Many2many('res.partner',  string="Axudantes")
    axudantes_ids = fields.Many2many('res.partner', ondelete='set null',string="Axudantes" )

    # @api.multi
    # def button_check_duracion(self):
    #     for sesion in self:
    #         if duracion < 1 or duracion > 4:
    #             raise Warning (
    #                 'A duración da %s ten que ser entre 1 e 4 horas' % sesion.name)
    #             return True