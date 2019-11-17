# -*- coding: utf-8 -*-
{
    'name': "student_test",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Thomas Edward",
    'website': "http://www.thomasedward.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'security/security_view.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/student_view.xml',
        'views/configuration_view.xml',
        'views/student_audit_log_view.xml',
        # 'views/report_saleorder.xml',
        'wizard/wiz_calc_age_view.xml',
        'report/student_report.xml',
        'report/student_profile.xml',
        'sequence.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}