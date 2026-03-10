# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    fabrication_project_id = fields.Many2one(
        "project.project",
        string="Project",
        tracking=True,
        copy=False,
        domain="[('company_id', 'in', [False, company_id])]",
    )

    @api.constrains("state", "picking_type_id", "fabrication_project_id")
    def _check_fabrication_project_required(self):
        for picking in self:
            if (
                picking.state not in ("draft", "cancel")
                and picking.picking_type_code in ("internal", "outgoing")
                and not picking.fabrication_project_id
            ):
                raise ValidationError(_("Internal/Outgoing transfer must have a Project."))
