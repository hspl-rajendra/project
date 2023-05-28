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
    'depends': ['base','mail','product','sale','mail'],#for use inherit
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',

        'data/patient_tag_data.xml',
        'data/patient.tag.csv',
        'data/sequence_data.xml',
        'data/mail_template_data.xml',
        'wizard/cancel_appointment_view.xml',
        'wizard/appointment_view_report.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/male_patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',
        'views/res_config_settings_views.xml',
        'views/operation.xml',
        'views/sale_order_view.xml',
        'views/lab.xml',
        'views/mailing_mailing_view.xml'
   ],
    'demo': [

    ],
 'assets': {
        'web._assets_primary_variables': [
            'account/static/src/scss/variables.scss',
        ],
        'web.assets_backend': [
            'vedant_hospital/static/js/pop.js',
        ],

    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}