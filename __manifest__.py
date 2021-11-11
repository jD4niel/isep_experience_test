# -*- coding: utf-8 -*-
{
    'name': "ISEP practice test",
    'description': """
        Module that saves contact experience based on skills
    """,
    'author': "Jesus Daniel Acosta Contreras",
    'website': "http://www.yourcompany.com",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base','contacts','web'],
    'data': [
        'security/ir.model.access.csv',
        'views/experience_partner_view.xml',
        'views/res_partner_view.xml',
        'wizard/add_skills_wizard_view.xml',
        'reports/partner_experience_view.xml',
        'reports/partner_experience_view_pdf.xml',
    ],
}
