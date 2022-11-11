# -*- coding: utf-8 -*-
{
    'name': "Venue Booking",

    'summary': """
        71 Milonayoton Venue Booking System""",

    'description': """
        This software is created for 71 Milonayoton Venue Booking System.
    """,

    'author': "Chinmay Roy",
    'website': "http://www.chinmayroy.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '15.0.1',
    'sequence': 1,

    # any module necessary for this one to work correctly
    'depends': ['base', 'web','website', 'website_mail','mail',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'data/venue_booking_email_template.xml',
        'views/venue_booking_list.xml',
        'views/booking_template_view.xml',
        'views/menus.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 0,
    'currency': 'USD',
    'license': 'LGPL-3',
    'contributors': [
        'Chinmay Roy <https://github.com/chinmayroy>',
    ],

    # Icon for this App
    'icon': '/venue_booking/static/img/venue_booking-icon.png',
}
