# -*- coding: utf-8 -*-

from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    fabrication_project_id = fields.Many2one(
        "project.project",
        string="Project",
        related="picking_id.fabrication_project_id",
        store=True,
        readonly=True,
    )
