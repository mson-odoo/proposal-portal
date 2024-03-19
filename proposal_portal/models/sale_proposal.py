# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleProposal(models.Model):
    _name = "sale.proposal"
    _inherit = "sale.order"
    _description = "Sale Proposal"

    name = fields.Char(default=lambda self: ('New'))

    state = fields.Selection(
        selection_add=[('draft', 'Draft'), ('sent', 'Sent'), ('sale', 'Confirm')])
    transaction_ids = fields.Many2many(
        relation='sale_proposal_transaction_rel', column1='sale_proposal_id')
    tag_ids = fields.Many2many(
        relation='sale_proposal_tag_rel', column1='proposal_id')
    proposal_status = fields.Selection(string="Proposal Status", selection=[('not_reviewed', 'Not Reviewed'), ('approved', 'Approved'), ('rejected', 'Rejected')], readonly=True, default="not_reviewed")
    sale_order = fields.Char(string="Sale Order", readonly=True)

    @api.model
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'sale.proposal') or ('New')
        res = super(SaleProposal, self).create(vals)
        return res
    
    def action_send_email(self):
        self.ensure_one()
        self.order_line._validate_analytic_distribution()
        mail_template = self.env.ref('proposal_portal.sale_proposal_email_template', raise_if_not_found=False)
        ctx = {
            'default_model': 'sale.proposal',
            'default_res_ids': self.ids,
            'default_template_id': mail_template.id if mail_template else None,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'default_email_layout_xmlid': 'mail.mail_notification_layout_with_responsible_signature',
            'proforma': self.env.context.get('proforma', False),
            'force_email': True,
        }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': ctx,
        }
