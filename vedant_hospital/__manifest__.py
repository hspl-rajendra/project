# -*- coding: utf-8 -*-
{
    'name' : 'vedant_management',
    'version' : '1.2',
    'sequence': 20,
    'author':'hspl',
    'category': 'Hospital',
    'author':'hspl',
    'website': 'https://www.odoo.com/app/invoicing',
    'description':"""Hospital managment system""",
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/male_patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml'

    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}