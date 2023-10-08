{
    'name': 'Modulo CA',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Módulo personalizado para clases y profesores',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/clase_views.xml',
        'views/profesor_views.xml',
        'views/salon_views.xml',
        'views/horario_views.xml',
        'views/feedback_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
}

