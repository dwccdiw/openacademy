from odoo import models, fields


class CursosReport(models.Model):
    _name = 'cursos.report'
    _description = 'Cursos Report'
    _auto = False

    # nomeCurso = fields.Char('nomeCurso')
    # descri = fields.Char('descripcion')
    # responsable = fields.Char('responsable_id')

    def init(self):
        self.env.cr.execute ("""
           CREATE OR REPLACE VIEW cursos_report AS
           (SELECT *
            FROM openacademy_curso 
           )
        """)
