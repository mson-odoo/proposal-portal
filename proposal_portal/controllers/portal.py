# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request


class CustomerPortal(http.Controller):
    
    @http.route(['/my/proposal/'], type="http", auth="public", website=True)
    def portal_proposal(self,**kw):
        proposal = request.env['sale.proposal'].sudo().search([])
        
        return request.render('proposal_portal.sale_proposal_portal_template', {proposal: proposal})