# PRD Traceability Matrix - Phase 1

| PRD ID | Requirement | Business Owner | Module / Custom Module | Dev Task ID | Test Case ID | UAT Case ID | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR-02 | Project Master | Project Control | `project`, `project_code_enforcement` | DEV-PROJ-01 | TC-PROJ-01..05 | UAT-01 | In Progress | Unique project code and assignment readiness |
| CUST-01 | Project Code Enforcement | PMO / Project Control | `project_code_enforcement` | DEV-ENF-01 | TC-ENF-01..08 | UAT-02, UAT-03, UAT-05 | In Progress | SO/PO/Issue/MO/WO/Invoice tagging and validation |
| FR-04 | Inventory & Warehouse | Warehouse | `stock`, `project_code_enforcement` | DEV-INV-01 | TC-INV-01..05 | UAT-02, UAT-03 | Planned | Focus on issue movements with project linkage |
| FR-05 | Manufacturing / Workshop | PPC / Production | `mrp`, `project_code_enforcement` | DEV-MRP-01 | TC-MRP-01..05 | UAT-03 | Planned | MO/WO project context enforced from early stage |
| FR-09 | Finance Basic | Finance | `account`, `project_code_enforcement` | DEV-FIN-01 | TC-FIN-01..04 | UAT-05 | Planned | Customer/vendor invoice posting requires project |

## Execution Notes

- Phase 1 starts with `CUST-01` as the hard data-governance gate.
- Test case IDs above are placeholders and should be expanded into executable test scripts.
- Status values should be updated per delivery wave (`Planned`, `In Progress`, `Done`).
