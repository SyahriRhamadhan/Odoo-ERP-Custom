# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class AccountMove(models.Model):
    _inherit = "account.move"

    fabrication_project_id = fields.Many2one(
        "project.project",
        string="Project",
        tracking=True,
        copy=False,
        domain="[('company_id', 'in', [False, company_id])]",
    )

    @api.constrains("state", "move_type", "fabrication_project_id")
    def _check_fabrication_project_required(self):
        target_types = {"out_invoice", "out_refund", "in_invoice", "in_refund"}
        for move in self:
            if move.state == "posted" and move.move_type in target_types and not move.fabrication_project_id:
                raise ValidationError(_("Posted customer/vendor invoices must have a Project."))
