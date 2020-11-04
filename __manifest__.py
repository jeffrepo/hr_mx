# -*- coding: utf-8 -*-
{
    'name': "hr_mx",

    'summary': """ Recursos humanos para MX """,

    'description': """
        Recursos humanos para MX
    """,

    'author': "JS",
    'website': "",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['hr','hr_payroll','base'],

    'data': [
        'views/report_wizard.xml',
        'views/hr_views.xml',
    ],
}
