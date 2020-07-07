# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import Warning
from odoo.exceptions import ValidationError


class sesion3(models.Model):
    _name = 'openacademy.sesion3' #IMPORTANTE é o nome da táboa
    _description = "Sesións dos cursos OpenAcademy 3"

    name = fields.Char (required=True, string="Nome da Sesión") #IMPORTANTE o campo ten que chamarse name
    data_sesion = fields.Datetime(string="Data da Sesión",default=lambda self: fields.Datetime.now())
    duracion = fields.Float(digits=(6, 2), string="Duración en horas", default=2)
    asentos = fields.Integer(string="Número de asentos" )
    curso_id = fields.Many2one('openacademy.curso3', ondelete='cascade', required=True,string="Título do Curso")
    asistentes_ids = fields.Many2many('res.partner', relation='openacademy_relacion_sesion3_res_partner',
                                     column1='sesion3_id',column2='asistente_id',
                                     string="Asistentes" )# Para definir nos a táboa relación, senón podería ser
    mes_date = fields.Char (compute="_cambio_data", size=15, store=True)
    enderezo = fields.Text (string="Local de xogo(Enderezo)")
    localidade = fields.Char (string="Localidade", size=40)
    pais = fields.Many2one ('res.country', string="País",
                            default=lambda self: self.env['res.country'].search ([('code', '=', 'ES')], limit=1))
    provincia = fields.Many2one ('res.country.state', string="Provincia", domain="[('country_id','=',pais)]",
                                 default=lambda self: self.env['res.country.state'].search (
                                     [('name', '=', 'Pontevedra')], limit=1))
    codigo_postal = fields.Char (size=5, string="Código Postal")

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
