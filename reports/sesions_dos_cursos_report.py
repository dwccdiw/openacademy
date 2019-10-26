from odoo import models, fields


class SesionsReport(models.Model):
    _name = 'sesions.dos.cursos.report'
    _description = 'Sesions Report'
    _auto = False

    # nomeCurso = fields.Char('c.nomeCurso')
    # nomeSesion = fields.Many2one('s.nomeSesion')
    # dataSesion = fields.Date('s.dataSesion')

    def init(self):
        self.env.cr.execute ("""
           CREATE OR REPLACE VIEW sesions_dos_cursos_report AS
           (SELECT 
            c.id,
            s.name,
            s.duracion,
            s.asentos,
            s.data_sesion,
            s.instructor_id
            FROM openacademy_curso c, openacademy_sesion s
            WHERE c.id = s.curso_id)
        """)
