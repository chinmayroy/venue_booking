# -*- coding: utf-8 -*-
{
    'name': "Venue Booking",

    'summary': """Venue Booking System""",

    'description': """This software is created for 71 Milonayoton Venue Booking System.""",

    'author': "Chinmay Roy",
    'website': "https://www.chinmayroy.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '15.0.1',
    'sequence': 1,

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'website', 'website_mail', 'mail', 'account',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'security/rules.xml',

        'data/venue_booked_email_template.xml',
        'data/venue_list_sequence.xml',

        'views/venue_booked_list.xml',
        'views/employee_information.xml',
        'views/venue_lists.xml',
        'views/venue_booking_team.xml',
        'views/venue_slot_list.xml',
        'views/venue_facilities.xml',
        'views/booking_web_template_view.xml',
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
