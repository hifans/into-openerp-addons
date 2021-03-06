# -*- coding: utf-8 -*-
##############################################################################
#
#
#    Copyright (C) 南京 ccdos ccdos@intoerp.com).
#
#
##############################################################################

{
    'name' : 'Double Validation on Sale',
    'version' : '1.1',
    'category': 'Sale Management',
    'depends' : ['base','sale'],
    'author' : 'OpenERP SA',
    'description': """
销售订单的 两次确认
=========================================================
销售人员 确认订单后，状态为  waiting_date

然后 应由 计划部（生产部） 人员 在此确认批准后，才会安排生产，
可扩充为 符合 一定条件才能被批准

    """,
    'website': 'http://www.intoerp.com',
    'data': [
        'security/security.xml',
        'sale_double_validation_workflow.xml',
        'sale_double_validation_view.xml',
    ],
    'test': [
    ],
    'demo': [],
    'installable': True,
    'auto_install': False
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
