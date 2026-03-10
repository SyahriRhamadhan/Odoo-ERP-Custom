# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    project_code = fields.Char(
        string="Project Code",
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _("New"),
        index=True,
    )

    _sql_constraints = [
        (
            "project_code_unique_per_company",
            "unique(project_code, company_id)",
            "Project code must be unique per company.",
        ),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get("project_code") or vals["project_code"] == _("New"):
                vals["project_code"] = self.env["ir.sequence"].next_by_code("project.project.code") or _("New")
        return super().create(vals_list)
