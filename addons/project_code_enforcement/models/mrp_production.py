# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    fabrication_project_id = fields.Many2one(
        "project.project",
        string="Project",
        tracking=True,
        copy=False,
        domain="[('company_id', 'in', [False, company_id])]",
    )

    @api.constrains("state", "fabrication_project_id")
    def _check_fabrication_project_required(self):
        for production in self:
            if production.state not in ("draft", "cancel") and not production.fabrication_project_id:
                raise ValidationError(_("A Manufacturing Order must have a Project."))
