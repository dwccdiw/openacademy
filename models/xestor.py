from odoo import fields, models


class xestor(models.Model):
    _inherit = 'res.partner'

    avatar = fields.Char (required=True, string="Avatar")

    # published_book_ids = fields.One2many(
    #     'openacademy.curso',  #  modelo
    #     'publisher_id',  # field for "this" on related model
    #     string='Published Books')
    #
    # book_ids = fields.Many2many(
    #     'library.book', string='Authored Books')