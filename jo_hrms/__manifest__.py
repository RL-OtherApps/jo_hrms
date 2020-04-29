# -*- coding: utf-8 -*-
{
    'name':'Jordanian HRMS Localization',
    'version': '0.1',
    'category': 'hr',
    'summary': 'Calculate Income Tax,Social Security, and Health Insurance',
    'description': "",
    'author': 'Ahmad Ibraheem',
    'depends': ['hr','hr_contract','hr_payroll' ,'account'],
    'data': ['views/jo_hrms_view.xml',
             'views/jo_hrms_payroll.xml',
             'data/jo_hrms_data.xml',
             'security/ir.model.access.csv',
             'security/jo_hrms_security.xml',
                ],
    'demo': ['data/jo_hrms_demo.xml'],

    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
