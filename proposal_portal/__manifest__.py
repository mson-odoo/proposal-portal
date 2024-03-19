# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Proposal Portal',
    'depends': ['sale_management', 'website'],
    'data':[
        'security/ir.model.access.csv',
        'views/sale_proposal_templates.xml',
        'data/sale_proposal_sequence.xml',
        'data/sale_proposal_mail_template.xml',
        'views/sale_proposal_views.xml',
        'views/sale_proposal_menus.xml',    
    ],
    'installable': True,
    'application': True,
}