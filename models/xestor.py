from odoo import fields, models


class xestor(models.Model):
    _inherit = 'res.partner'# como  non lle proporcioamos  _name facemos herdanza por extensión (herdanza de clase)
                            # por tanto non se crea unha nova clase e os atributos engadense na clase pai
                            # No xml das vistas temos que extender as vistas da clase pai
    avatar = fields.Char (required=True, string="Avatar")
    apelidos = fields.Char( required=True, string="Apelidos")

