# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    fabrication_project_id = fields.Many2one(
        "project.project",
        string="Project",
        tracking=True,
        copy=False,
        domain="[('company_id', 'in', [False, company_id])]",
    )

    @api.constrains("state", "fabrication_project_id")
    def _check_fabrication_project_required(self):
        for order in self:
            if order.state in ("purchase", "done") and not order.fabrication_project_id:
                raise ValidationError(_("A confirmed Purchase Order must have a Project."))
