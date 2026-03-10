# -*- coding: utf-8 -*-
{
    "name": "Project Code Enforcement",
    "summary": "Enforce project tagging on core heavy-fabrication transactions.",
    "version": "17.0.1.0.0",
    "category": "Project",
    "author": "Arus Digital",
    "license": "LGPL-3",
    "depends": [
        "project",
        "sale_management",
        "purchase",
        "stock",
        "mrp",
        "account",
    ],
    "data": [
        "data/ir_sequence_data.xml",
        "views/project_project_views.xml",
        "views/sale_order_views.xml",
        "views/purchase_order_views.xml",
        "views/stock_picking_views.xml",
        "views/mrp_production_views.xml",
        "views/account_move_views.xml",
    ],
    "installable": True,
    "application": False,
}
