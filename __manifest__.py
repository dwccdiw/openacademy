# -*- coding: utf-8 -*-
{
  'name': 'openacademy',
  'summary': 'Xestionando a formación',
  'description': 'Formación de proba en varias liñas',
  'author': 'odoo e eu',
  'website': 'http://www.antonio.com',
  'category': 'Educacion',
  'version': '0.1',
  'depends': ['base'],# módulos dos que depende o noso módulo
  'data': [
      'security/ir.model.access.csv',
      'views/cursos.xml',
      'views/sesions.xml',
  #    'views/templates.xml', # Só a primeira vez
      'reports/cursos_report.xml',
      'reports/sesions_dos_cursos_report.xml',
  ],
  'images': [],
  'license': 'AGPL-3',
  'installable': True,
  'application': True,
  'auto_install': False,

    # Só se carga en modo demostración
    # 'demo': [
    #  'demo/demo.xml',
}
