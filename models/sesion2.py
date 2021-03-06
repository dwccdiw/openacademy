# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import Warning
from odoo.exceptions import ValidationError


class sesion2(models.Model):
    _name = 'openacademy.sesion2' #IMPORTANTE é o nome da táboa
    _description = "Sesións dos cursos OpenAcademy "

    name = fields.Char (required=True, string="Nome da Sesión") #IMPORTANTE o campo ten que chamarse name
    data_sesion = fields.Datetime(string="Data da Sesión",default=lambda self: fields.Datetime.now())
    duracion = fields.Float(digits=(6, 2), string="Duración en horas", default=2)
    asentos = fields.Integer(string="Número de asentos" )
    instructor_id = fields.Many2one('res.partner',string="Docente")
    nacionalidade = fields.Many2one ('res.country', string='Nacionalidade')
    foto = fields.Binary (string='Foto')
    sexo = fields.Selection ([('male', 'Home'), ('female', 'Muller'), ('others', 'Outros')], string='Sexo')
    autorizado = fields.Boolean (string="¿Autorizado?", default=True)
    curso_id = fields.Many2one('openacademy.curso2', ondelete='cascade', required=True,string="Título do Curso")

    # attendee_ids = fields.Many2many ('management.student', relation='your_table_name', column1='course_id',
    #                                  column2='student_id', string="Attendees")
    axudantes_ids = fields.Many2many('res.partner', relation='openacademy_relacion_sesion2_res_partner',
                                     column1='sesion2_id',column2='axundante_id',
                                     string="Axudantes" )# Para definir nos a táboa relación, senón podería ser
    # axudantes_ids = fields.Many2many('res.partner', ondelete='set null',string="Axudantes" )
    moeda_id = fields.Many2one ('res.currency')
    custo_por_hora = fields.Monetary ("Custo por hora", 'moeda_id')
    mes_date = fields.Char (compute="_cambio_data", size=15, store=True)

    def button_check_duracion(self): # é necesario engadir no xml da vista no header o botón
        #self.ensure_one ()
        for rexistro in self:
            if rexistro.duracion < 1 or rexistro.duracion > 4:
                raise Warning (
                    'A duración da %s ten que ser entre 1 e 4 horas' % rexistro.name)
            else:
                raise Warning (
                    'Duración da %s correcta' % rexistro.name)
                return True


    @api.constrains ('data_sesion')
    def _valor(self):
        for rexistro in self:
            if (rexistro.curso_id.data_inicio > rexistro.data_sesion) or (
                    rexistro.curso_id.data_fin < rexistro.data_sesion):
                raise ValidationError (
                    "A DATA DA SESIÓN %s ten que estar entre '%s' e '%s'" % (
                    rexistro.name, rexistro.curso_id.data_inicio, rexistro.curso_id.data_fin))


    @api.constrains ('duracion')
    def _constrain_duracion_sesion(self):
        for rexistro in self:
            if rexistro.duracion < 1 or rexistro.duracion > 4:
                raise ValidationError (
                    'A duración da %s ten que ser entre 1 e 4 horas' % rexistro.name)
