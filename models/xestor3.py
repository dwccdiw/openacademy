from odoo import fields, models


class xestor3(models.Model):
    _name = 'openacademy.xestor3'# como lle proporcioamos  _name crea unha nova táboa
    _inherits = {'res.partner': 'partner_id'}# Como poñemos _inherits en vez de _inherit facemos herdanza por delegación
                                            # e na definición creamos unha relación coa táboa pai
                                            # No xml das vistas temos que extender as vistas da clase pai
    partner_id = fields.Many2one ('res.partner')
    avatar3 = fields.Char (required=True, string="Avatar3")


