# -*- coding: utf-8 -*-

from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase


class TestProjectCodeEnforcement(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner = cls.env["res.partner"].create({"name": "Test Customer"})
        cls.vendor = cls.env["res.partner"].create({"name": "Test Vendor", "supplier_rank": 1})
        cls.project = cls.env["project.project"].create({"name": "Project Alpha"})
        cls.uom_unit = cls.env.ref("uom.product_uom_unit")
        cls.product = cls.env["product.product"].create(
            {
                "name": "Test Manufactured Product",
                "type": "product",
                "uom_id": cls.uom_unit.id,
                "uom_po_id": cls.uom_unit.id,
            }
        )
        location_stock = cls.env.ref("stock.stock_location_stock", raise_if_not_found=False)
        location_production = cls.env.ref("stock.stock_location_production", raise_if_not_found=False)
        if not location_stock:
            location_stock = cls.env["stock.location"].create(
                {"name": "Stock", "usage": "internal", "company_id": cls.env.company.id}
            )
        if not location_production:
            location_production = cls.env["stock.location"].create(
                {"name": "Production", "usage": "internal", "company_id": cls.env.company.id}
            )

        cls.internal_picking_type = cls.env["stock.picking.type"].search([("code", "=", "internal")], limit=1)
        if not cls.internal_picking_type:
            cls.internal_picking_type = cls.env["stock.picking.type"].create(
                {
                    "name": "Internal Transfer",
                    "code": "internal",
                    "sequence_code": "INTT",
                    "default_location_src_id": location_stock.id,
                    "default_location_dest_id": location_production.id,
                    "company_id": cls.env.company.id,
                }
            )

        cls.outgoing_picking_type = cls.env["stock.picking.type"].search([("code", "=", "outgoing")], limit=1)
        cls.mrp_picking_type = cls.env["stock.picking.type"].search(
            [("code", "=", "mrp_operation"), ("company_id", "=", cls.env.company.id)], limit=1
        )
        expense_account = cls.env["account.account"].search(
            [("company_id", "=", cls.env.company.id), ("account_type", "=", "expense")], limit=1
        )
        income_account = cls.env["account.account"].search(
            [("company_id", "=", cls.env.company.id), ("account_type", "=", "income")], limit=1
        )
        if not expense_account:
            expense_account = cls.env["account.account"].create(
                {
                    "name": "Test Expense",
                    "code": "X600000",
                    "account_type": "expense",
                    "company_id": cls.env.company.id,
                }
            )
        if not income_account:
            income_account = cls.env["account.account"].create(
                {
                    "name": "Test Income",
                    "code": "X700000",
                    "account_type": "income",
                    "company_id": cls.env.company.id,
                }
            )

        cls.purchase_journal = cls.env["account.journal"].search([("type", "=", "purchase")], limit=1)
        if not cls.purchase_journal:
            cls.purchase_journal = cls.env["account.journal"].create(
                {
                    "name": "Test Purchase Journal",
                    "code": "TPJ",
                    "type": "purchase",
                    "company_id": cls.env.company.id,
                    "default_account_id": expense_account.id,
                }
            )

        cls.sales_journal = cls.env["account.journal"].search([("type", "=", "sale")], limit=1)
        if not cls.sales_journal:
            cls.sales_journal = cls.env["account.journal"].create(
                {
                    "name": "Test Sales Journal",
                    "code": "TSJ",
                    "type": "sale",
                    "company_id": cls.env.company.id,
                    "default_account_id": income_account.id,
                }
            )

    def test_tc_enf_001_project_code_auto_generated(self):
        project = self.env["project.project"].create({"name": "Project With Auto Code"})
        self.assertTrue(project.project_code)
        self.assertNotEqual(project.project_code, "New")

    def test_tc_enf_002_sale_order_requires_project_on_confirmed(self):
        order = self.env["sale.order"].create({"partner_id": self.partner.id})
        with self.assertRaises(ValidationError):
            order.write({"state": "sale"})

    def test_tc_enf_003_sale_order_passes_with_project(self):
        order = self.env["sale.order"].create(
            {"partner_id": self.partner.id, "fabrication_project_id": self.project.id}
        )
        order.write({"state": "sale"})
        self.assertEqual(order.state, "sale")

    def test_tc_enf_004_purchase_order_requires_project_on_confirmed(self):
        order = self.env["purchase.order"].create({"partner_id": self.vendor.id})
        with self.assertRaises(ValidationError):
            order.write({"state": "purchase"})

    def test_tc_enf_005_purchase_order_passes_with_project(self):
        order = self.env["purchase.order"].create(
            {"partner_id": self.vendor.id, "fabrication_project_id": self.project.id}
        )
        order.write({"state": "purchase"})
        self.assertEqual(order.state, "purchase")

    def test_tc_enf_006_internal_picking_requires_project(self):
        picking = self.env["stock.picking"].create({"picking_type_id": self.internal_picking_type.id})
        with self.assertRaises(ValidationError):
            picking.write({"state": "confirmed"})

    def test_tc_enf_007_internal_picking_passes_with_project(self):
        picking = self.env["stock.picking"].create(
            {
                "picking_type_id": self.internal_picking_type.id,
                "fabrication_project_id": self.project.id,
            }
        )
        picking.write({"state": "confirmed"})
        self.assertEqual(picking.state, "confirmed")

    def test_tc_enf_008_mrp_production_requires_project(self):
        self.assertTrue(self.mrp_picking_type, "MRP operation type must exist for MRP tests.")
        production = self.env["mrp.production"].create(
            {
                "product_id": self.product.id,
                "product_qty": 1.0,
                "product_uom_id": self.uom_unit.id,
                "picking_type_id": self.mrp_picking_type.id,
            }
        )
        with self.assertRaises(ValidationError):
            production.write({"state": "progress"})

    def test_tc_enf_009_mrp_production_passes_with_project(self):
        self.assertTrue(self.mrp_picking_type, "MRP operation type must exist for MRP tests.")
        production = self.env["mrp.production"].create(
            {
                "product_id": self.product.id,
                "product_qty": 1.0,
                "product_uom_id": self.uom_unit.id,
                "picking_type_id": self.mrp_picking_type.id,
                "fabrication_project_id": self.project.id,
            }
        )
        production.write({"state": "progress"})
        self.assertEqual(production.state, "progress")

    def test_tc_enf_010_account_move_requires_project_when_posted(self):
        move = self.env["account.move"].create(
            {
                "move_type": "out_invoice",
                "partner_id": self.partner.id,
                "journal_id": self.sales_journal.id,
            }
        )
        with self.assertRaises(ValidationError):
            move.write({"state": "posted"})

    def test_tc_enf_011_account_move_passes_with_project(self):
        move = self.env["account.move"].create(
            {
                "move_type": "in_invoice",
                "partner_id": self.vendor.id,
                "journal_id": self.purchase_journal.id,
                "fabrication_project_id": self.project.id,
            }
        )
        move.write({"state": "posted"})
        self.assertEqual(move.state, "posted")
