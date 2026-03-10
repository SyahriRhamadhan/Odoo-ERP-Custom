# -*- coding: utf-8 -*-

from odoo import fields, models


class MrpWorkorder(models.Model):
    _inherit = "mrp.workorder"

    fabrication_project_id = fields.Many2one(
        "project.project",
        string="Project",
        related="production_id.fabrication_project_id",
        store=True,
        readonly=True,
    )
