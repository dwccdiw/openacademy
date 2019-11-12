from odoo import fields, models


class xestor2(models.Model):
    _name = 'openacademy.xestor2'# proporcionamos  _name entón facemos prototipo de herdanza
                            # por tanto  se crea unha nova táboa
                            # No xml das vistas temos que extender as vistas da clase pai
    _inherit = 'res.partner'  # como  non lle proporcioamos  _name facemos herdanza por extensión (herdanza de clase)
    avatar2 = fields.Char (required=True, string="Avatar2")

