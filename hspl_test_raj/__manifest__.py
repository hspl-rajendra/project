# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hspl Test Raj',
    'version' : '1.2',
    'summary': 'Hspl Test Raj',
    'sequence': 10,
    'description': """
      test  module in odoo in hspl
     """,
    'category': '',
    'website': 'https://www.odoo.com/app/invoicing',
    'images' : [],
    'depends' : ['base','sale','portal'],
    'data': [
        'security/ir.model.access.csv',
        'security/secuirity.xml',

         'wizard/vendor_view.xml',
         'views/membership_leve.xml',

         'views/res_partner_views.xml',
         'views/sale_order_view.xml',
         'views/inherit_template.xml',
         'views/membership_s.xml',
         # 'views/res_partners_views.xml',

    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
