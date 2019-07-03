# -*- coding: utf-8 -*-

{
    'name': 'SQL Export',
    'version': '10.0.1',
    'author': 'Ivan Porras',
    'website': 'http://www.grupoalvamex.com',
    'license': 'AGPL-3',
    'category': 'Dashboard',
    'summary': 'Export data in csv file with SQL requests',
    'depends': [
        'sql_request_abstract',
    ],
    'data': [
        'views/sql_export_view.xml',
        'wizard/wizard_file_view.xml',
        'security/sql_export_security.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/sql_export.xml',
    ],
    'installable': True,
    }
