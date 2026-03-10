# PRD — Odoo Community untuk Perusahaan Heavy Fabrication Batam

## 1. Ringkasan Produk
Dokumen ini mendefinisikan Product Requirements Document (PRD) untuk implementasi Odoo Community pada perusahaan dummy **PT Batam Marine Pipe & Fabrication**, yaitu perusahaan fabrikasi berbasis proyek yang bergerak di bidang pipe spool fabrication, steel structure/skid fabrication, serta ship repair/modification. Sistem ditujukan untuk mengintegrasikan proses komersial, engineering, procurement, inventory, workshop execution, QC, maintenance, HR, dan finance dasar dalam satu platform yang dapat dikembangkan bertahap dengan bantuan Codex.

## 2. Latar Belakang
Perusahaan heavy fabrication di Batam memiliki karakter berbeda dari manufaktur mass production biasa. Operasi utamanya berbasis project order, engineer-to-order, make-to-order, dan repair/service. Tantangan yang paling sering muncul adalah revisi drawing, keterlambatan material, traceability heat number/material certificate, bottleneck workshop, quality rework, kontrol biaya proyek, dan ketidaksinkronan data antar divisi.

Tujuan sistem adalah menjadikan Odoo sebagai **single operational backbone** untuk transaksi, kontrol proses, dan sumber data analitik. Sistem tidak harus menyelesaikan semua kebutuhan industri pada fase pertama; fase awal fokus pada proses inti yang paling menentukan visibilitas dan akurasi data.

## 3. Tujuan Bisnis
1. Mengurangi silo data antara Sales, Engineering, Procurement, Warehouse, Workshop, QC, HR, dan Finance.
2. Meningkatkan akurasi status proyek, status material, dan status produksi.
3. Membentuk fondasi job costing per project.
4. Menyediakan dashboard manajemen yang dapat dipercaya.
5. Menyiapkan arsitektur yang siap ditambah modul custom untuk traceability, FTZ workflow, progress billing, dan quality dossier.

## 4. Objective Produk
Sistem harus mampu:
- mencatat inquiry sampai order aktif,
- membentuk master project dan cost code,
- mengelola material procurement dan stock by location,
- mengelola work order dasar pada workshop,
- mencatat actual issue material dan actual labor/time,
- mencatat inspeksi QC dasar dan rework,
- mengelola maintenance equipment,
- mengelola employee master, attendance, dan struktur organisasi,
- menyediakan laporan operasional dan dashboard KPI inti.

## 5. Non-Goals Fase Awal
Hal berikut **tidak wajib** selesai pada fase pertama:
- integrasi CEISA/PPFTZ/FTZ customs,
- e-signature kontrak formal,
- payroll industrial kompleks,
- MTC dossier otomatis end-to-end,
- NDT register tingkat lanjutan,
- mobile barcode terminal penuh,
- BI enterprise-grade penuh,
- costing estimasi tender yang sangat rinci seperti software estimator khusus.

## 6. User & Divisi
### 6.1 Top Management
Kebutuhan: melihat order book, profitability, bottleneck, overdue material, NCR, cash position.

### 6.2 Sales / Tender
Kebutuhan: lead, quotation, revision quotation, order conversion, customer history.

### 6.3 Project Control / PPC
Kebutuhan: project code, schedule, material readiness, work order status, progress vs plan.

### 6.4 Engineering & Document Control
Kebutuhan: drawing register, revision tracking, BoM reference, approved-for-production indicator.

### 6.5 Procurement
Kebutuhan: PR/RFQ/PO, vendor comparison, ETA, overdue PO, subcontract tracking.

### 6.6 Warehouse & Logistics
Kebutuhan: receiving, putaway, stock transfer, issue by project, finished goods dispatch, stock count.

### 6.7 Workshop / Production
Kebutuhan: work order, work center, start-stop execution, consumption, output qty, hold status, rework.

### 6.8 QA/QC
Kebutuhan: incoming inspection, in-process check, final release, NCR, rework closure.

### 6.9 Maintenance
Kebutuhan: equipment register, preventive maintenance schedule, corrective request, downtime log.

### 6.10 HRGA
Kebutuhan: employee master, structure, attendance, shift, approval flow dasar.

### 6.11 Finance & Accounting
Kebutuhan: customer/vendor invoice dasar, AP/AR, project-linked cost visibility, posted transaction control.

## 7. Scope Modul Odoo Community
### In Scope — Fase 1
- CRM
- Sales
- Purchase
- Inventory
- Manufacturing
- Project
- Employees
- Attendances
- Maintenance
- Invoicing / Accounting basic
- Documents (jika tersedia melalui addon komunitas yang dipilih)

### In Scope — Custom Layer Prioritas
- project code enforcement
- simple job costing per project
- engineering register sederhana
- QC checklist dasar
- NCR & rework basic
- dashboard operasional/manajemen

### Out of Scope — Fase 1
- PLM enterprise-style lengkap
- Quality enterprise-style lengkap jika tidak memakai addon komunitas
- payroll penuh industri
- FTZ integration live
- vendor portal penuh

## 8. Proses Bisnis Target (To-Be)
### 8.1 Inquiry to Order
1. Sales membuat lead/opportunity.
2. Estimator menyiapkan quotation dan asumsi biaya.
3. Jika approved, Sales Order dibuat.
4. Sistem membuat project code dan project shell.

### 8.2 Engineering to Procurement
1. Engineering mengunggah drawing register.
2. Engineering mengisi material take-off/BoM.
3. PPC memeriksa shortage.
4. Procurement membuat RFQ dan PO.

### 8.3 Receiving to Warehouse
1. Barang diterima di Receiving.
2. Incoming inspection dilakukan.
3. Barang lolos masuk lokasi stock.
4. Barang gagal masuk QC Hold/Reject.

### 8.4 Planning to Workshop Execution
1. PPC membuat Manufacturing Order / Work Order.
2. Work order dibagi ke work center: cutting, fit-up, welding, assembly, painting, packing.
3. Operator mulai work order.
4. Material di-issue ke work order / project.
5. Output berpindah ke stage berikutnya.

### 8.5 QC to Rework / Release
1. QC melakukan check pada titik inspeksi.
2. Jika pass, item released ke next step.
3. Jika fail, NCR dibuat.
4. Rework order dibuka.
5. Setelah pass, item ditutup.

### 8.6 Delivery to Billing
1. Finished goods dipindah ke dispatch.
2. Delivery order dan packing list dibuat.
3. Finance membuat invoice sesuai milestone/termin dasar.
4. Pembayaran direkam pada AR.

### 8.7 Maintenance
1. Equipment terdaftar per lokasi.
2. Preventive maintenance dijadwalkan.
3. Operator/foreman dapat membuat corrective request.
4. MTBF/MTTR dicatat untuk analisis.

### 8.8 HR & Attendance
1. HR membuat employee master.
2. Supervisor memetakan employee ke departemen dan shift.
3. Attendance tercatat.
4. Overtime approval dasar dilakukan.

## 9. Master Data
### 9.1 Master Organisasi
- company
- department
- cost center
- project code
- work center
- warehouse / location

### 9.2 Master Partner
- customer
- vendor
- subcontractor
- tax data
- payment term
- currency

### 9.3 Master Employee
- employee ID
- name
- department
- title
- shift
- cost rate
- certification
- expiry date
- supervisor

### 9.4 Master Material / Product
- internal code
- product category
- UoM
- stock type
- standard cost
- preferred vendor
- lead time
- lot/serial tracking flag
- project relevance flag

### 9.5 Master Workshop
- work center
- standard capacity
- setup time
- run time assumption
- maintenance policy

### 9.6 Master Quality
- inspection type
- defect type
- NCR category
- disposition type
- acceptance criteria

## 10. Functional Requirements
## FR-01 CRM & Sales
Sistem harus memungkinkan user membuat lead, opportunity, quotation, revisi quotation, dan sales order.

**Acceptance Criteria**
- user dapat membuat lead baru,
- quotation memiliki version/revision field,
- sales order hanya bisa dibuat jika quotation approved,
- setiap sales order otomatis memiliki project reference.

## FR-02 Project Master
Sistem harus membuat project master untuk setiap order aktif.

**Acceptance Criteria**
- project code unik,
- project manager dapat di-assign,
- budget summary dapat disimpan,
- semua transaksi pembelian dan issue material dapat ditautkan ke project.

## FR-03 Procurement
Sistem harus mendukung RFQ, PO, vendor selection, ETA, dan overdue monitoring.

**Acceptance Criteria**
- RFQ dapat dikonversi menjadi PO,
- PO memiliki project reference,
- ETA tersimpan,
- report overdue PO tersedia.

## FR-04 Inventory & Warehouse
Sistem harus mendukung receiving, transfer antar lokasi, issue ke project/work order, stock count, dan dispatch.

**Acceptance Criteria**
- barang dapat diterima ke receiving,
- barang dapat dipindah ke lokasi final,
- stock issue wajib menyertakan project,
- stock opname menghasilkan variance report.

## FR-05 Manufacturing / Workshop
Sistem harus mendukung MO/WO, work center, actual execution, labor/time basic, material consumption, dan output status.

**Acceptance Criteria**
- work order dapat dibuat per project/package,
- operator bisa start/stop,
- material consumption tercatat,
- output berpindah status,
- report plan vs actual tersedia.

## FR-06 QC & NCR
Sistem harus mendukung incoming inspection, in-process inspection, final inspection, NCR, dan rework closure dasar.

**Acceptance Criteria**
- QC check dapat dibuat per transaksi,
- item gagal dapat dipindah ke QC Hold,
- NCR punya status open/in review/closed,
- rework dapat ditautkan ke project/work order.

## FR-07 Maintenance
Sistem harus mendukung equipment register, PM schedule, corrective request, downtime log.

**Acceptance Criteria**
- equipment dapat didaftarkan,
- PM otomatis jatuh tempo berdasarkan frekuensi,
- corrective request dapat dibuat,
- downtime report tersedia.

## FR-08 Employees & Attendance
Sistem harus mendukung employee master, organization structure, attendance, dan overtime request dasar.

**Acceptance Criteria**
- employee master lengkap,
- supervisor relation tersimpan,
- attendance dapat direkap per hari/bulan,
- overtime request punya approval status.

## FR-09 Finance Basic
Sistem harus mendukung customer invoice, vendor bill, payment registration, dan report AP/AR dasar.

**Acceptance Criteria**
- invoice dapat dibuat dari sales order/milestone manual,
- vendor bill dapat dikaitkan ke PO/project,
- AR aging tersedia,
- AP aging tersedia.

## FR-10 Dashboard Manajemen
Sistem harus menyediakan dashboard untuk direksi dan dashboard operasional untuk middle management.

**Acceptance Criteria**
- dashboard commercial tersedia,
- dashboard project profitability tersedia,
- dashboard operations tersedia,
- data dashboard hanya mengambil transaksi yang valid/posted/confirmed.

## 11. Kebutuhan Custom Prioritas
### CUST-01 Project Code Enforcement
Semua transaksi utama harus membawa project code: SO, PO, goods issue, MO/WO, vendor bill, customer invoice.

### CUST-02 Simple Job Costing
Dashboard job costing harus menghitung minimal:
- material cost actual
- labor cost actual
- subcontract cost actual
- overhead proxy
- revenue actual
- gross margin

### CUST-03 Engineering Register
Dibutuhkan register untuk:
- drawing no
- revision
- issue date
- approved for fabrication
- linked project/package

### CUST-04 QC Checklist & NCR
Diperlukan form QC dasar dan NCR lifecycle sederhana.

### CUST-05 Rework Tracking
Diperlukan penandaan work order rework dan biaya rework.

### CUST-06 Dashboard KPI
Dashboard harus mendukung filter per project, date range, customer, work center.

## 12. Data Model Inti
### Entity Kunci
- Project
- Sales Order
- Quotation Revision
- Drawing Register
- BoM / MTO
- Purchase Order
- Goods Receipt
- Stock Move
- Work Order
- QC Check
- NCR
- Rework Order
- Equipment
- Maintenance Request
- Employee
- Attendance
- Vendor Bill
- Customer Invoice

### Relasi Penting
- 1 Project memiliki banyak SO/PO/WO/QC/NCR/Invoice
- 1 Work Order terhubung ke 1 Project dan 1 Work Center
- 1 QC Check dapat terhubung ke Receipt atau WO
- 1 NCR dapat terhubung ke 1 Project dan 1 WO/Receipt
- 1 Employee terhubung ke Department dan Cost Rate

## 13. Dashboard KPI
## 13.1 Direksi
### Commercial
- inquiry count
- quotation submitted
- quote win rate
- order intake
- order book
- average quoted margin

### Project Profitability
- contract value
- budget cost
- actual cost
- gross profit
- gross margin %
- cost variance
- progress vs billing

### Operations
- plan vs actual completion
- work order completion rate
- labor efficiency
- rework rate
- scrap rate
- bottleneck work center

### Supply Chain
- material readiness by project
- overdue PO
- vendor on-time delivery
- stock accuracy
- dead stock value

### Quality & Maintenance
- NCR count
- NCR aging
- first pass yield
- downtime hours
- MTBF
- MTTR

### Finance
- AR aging
- AP aging
- invoiced vs unbilled
- cash in vs cash out (summary)

## 13.2 Middle Management
- work order backlog
- daily production progress
- receiving pending inspection
- project shortage list
- maintenance due list
- attendance exception list

## 14. Arsitektur Implementasi yang Disarankan
- Odoo Community sebagai system of record transaksi
- custom module terpisah per domain (project_costing, engineering_register, qc_basic, ncr_rework, executive_dashboard)
- dashboard eksekutif dapat memakai Odoo internal lebih dulu, lalu dipisah ke BI tool setelah data matang
- semua custom wajib modular, tidak monolitik

## 15. Urutan Pengerjaan untuk Codex
Pengerjaan dibagi menjadi beberapa gelombang agar tetap terkendali.

## Phase 0 — Foundation
**Tujuan:** menyiapkan fondasi data dan aturan.

Deliverable:
- finalisasi scope
- environment dev/staging
- struktur repository
- naming convention
- project code convention
- role matrix
- master data template CSV

Definition of Done:
- repo hidup,
- branch strategy ada,
- staging dapat diakses,
- master data template approved.

## Phase 1 — Core Master Data & Access
**Tujuan:** membangun fondasi user, role, organisasi, warehouse, work center, project code.

Task urutan:
1. setup company, departments, roles
2. setup warehouse & locations
3. setup work centers
4. setup employee master extension
5. setup project master & project code rule
6. seed master data awal

Definition of Done:
- user dapat login sesuai role,
- project code unik,
- location dan work center siap dipakai,
- master data dummy ter-load.

## Phase 2 — Sales to Project Activation
**Tujuan:** mengaktifkan proses inquiry sampai project opening.

Task urutan:
1. configure CRM & Sales
2. custom quotation revision field
3. SO to project shell creation
4. approval state basic
5. document attachment convention

Definition of Done:
- lead -> quotation -> SO berjalan,
- SO otomatis membuat project shell,
- semua record punya audit trail dasar.

## Phase 3 — Procurement & Inventory
**Tujuan:** memastikan alur material bekerja.

Task urutan:
1. configure vendors & purchasing
2. project-linked PO
3. receiving flow
4. incoming QC hold location
5. stock transfer by location
6. material issue by project
7. stock count flow

Definition of Done:
- PO sampai receipt berjalan,
- stock by location akurat,
- issue material wajib pakai project,
- shortage report bisa dilihat.

## Phase 4 — Workshop / Manufacturing
**Tujuan:** membangun alur produksi dasar.

Task urutan:
1. configure BoM & routings dasar
2. create work centers
3. MO/WO flow
4. operator execution basic
5. material consumption
6. output completion
7. plan vs actual report

Definition of Done:
- WO bisa dijalankan ujicoba end-to-end,
- consumption tercatat,
- output pindah stage,
- progress workshop terlihat.

## Phase 5 — QC, NCR, Rework
**Tujuan:** menutup celah kualitas.

Task urutan:
1. QC checklist basic
2. incoming QC flow
3. in-process QC flow
4. final QC flow
5. NCR object & status
6. rework relation to WO
7. defect report

Definition of Done:
- item gagal bisa di-hold,
- NCR dapat dibuka dan ditutup,
- rework muncul di report.

## Phase 6 — Maintenance & HR Attendance
**Tujuan:** melengkapi kemampuan operasional.

Task urutan:
1. equipment register
2. PM schedule
3. corrective maintenance request
4. employee structure
5. attendance & overtime request
6. summary report

Definition of Done:
- equipment aktif,
- PM jatuh tempo muncul,
- attendance terlapor,
- overtime request dapat diuji.

## Phase 7 — Finance Basic & Dashboard
**Tujuan:** menyajikan hasil bisnis dan dashboard.

Task urutan:
1. invoice basic
2. vendor bill project tagging
3. AR/AP report
4. simple job costing aggregation
5. dashboard direksi
6. dashboard middle management
7. data reconciliation round

Definition of Done:
- invoice dan bill muncul,
- margin dasar per project muncul,
- dashboard lolos rekonsiliasi.

## 16. Mekanisme Pengecekan PRD agar Tetap On Track
Pendekatannya bukan hanya QA teknis, tetapi **PRD verification loop**.

### 16.1 Tiga Level Verifikasi
#### Level A — Requirement Check
Memastikan setiap requirement punya:
- objective jelas
- actor jelas
- input/output jelas
- acceptance criteria jelas
- owner jelas

#### Level B — Functional Check
Memastikan flow berjalan secara end-to-end sesuai skenario user.

#### Level C — Data Trust Check
Memastikan angka pada dashboard cocok dengan transaksi sumber.

## 16.2 PRD Traceability Matrix
Buat tabel wajib berikut:
- PRD ID
- Requirement Name
- Business Owner
- Module / Custom Module
- Dev Task ID
- Test Case ID
- UAT Case ID
- Status
- Notes

Contoh:
- FR-03 Procurement -> DEV-PO-01/02/03 -> TC-PO-01 sampai TC-PO-05 -> UAT-PROC-01
- FR-10 Dashboard -> DEV-DASH-01/02 -> TC-DASH-01 sampai TC-DASH-06 -> UAT-MGMT-01

## 16.3 Unit Testing versi PRD
Di sini “unit testing” bukan hanya level Python test, tetapi **unit of requirement test**.

Setiap FR/CUST harus punya 5 lapis pengujian:
1. **Config Test** — apakah konfigurasi dasar benar.
2. **Transaction Test** — apakah user dapat menjalankan transaksi.
3. **Validation Test** — apakah rule wajib dipaksa sistem.
4. **Negative Test** — apakah skenario salah ditolak.
5. **Report Test** — apakah data hasil muncul benar di report/dashboard.

### Contoh untuk FR-04 Inventory
- Config Test: lokasi gudang dan operation type tersedia.
- Transaction Test: user bisa menerima barang dan issue ke project.
- Validation Test: issue tanpa project code ditolak.
- Negative Test: qty issue melebihi available stock ditolak/terdeteksi.
- Report Test: stock card dan project material report berubah sesuai transaksi.

### Contoh untuk CUST-02 Job Costing
- Config Test: mapping cost source aktif.
- Transaction Test: PO, stock issue, labor time, vendor bill masuk ke project.
- Validation Test: transaksi tanpa project tidak ikut job costing.
- Negative Test: duplicate posting tidak menggandakan cost.
- Report Test: gross margin dashboard cocok dengan sumber data.

## 16.4 Test Pyramid yang Disarankan
### Level 1 — Technical Unit Test
Untuk model, method, computed field, access rule, constraint.

### Level 2 — Integration Test
Untuk flow lintas modul: SO -> Project -> PO -> Receipt -> WO -> QC -> Invoice.

### Level 3 — Business Scenario Test
Untuk skenario nyata perusahaan.

### Level 4 — UAT
Dijalankan oleh user per divisi.

## 16.5 Contoh Skenario UAT Wajib
### UAT-01 Inquiry to Order
Sales membuat inquiry, quotation, revisi quotation, lalu convert menjadi SO dan project.

### UAT-02 Material Purchase to Receipt
Procurement membuat PO, warehouse menerima material, QC incoming memutuskan pass/fail.

### UAT-03 Workshop Execution
PPC membuat WO, operator start/stop, issue material, output selesai.

### UAT-04 QC & Rework
QC fail, NCR dibuat, rework dilakukan, item pass.

### UAT-05 Delivery to Invoice
Barang dispatch, invoice terbit, AR muncul.

### UAT-06 Maintenance
PM jatuh tempo, corrective request dibuat, downtime tercatat.

### UAT-07 Dashboard Reconciliation
Nilai dashboard dibandingkan dengan transaksi sumber dan disetujui owner bisnis.

## 16.6 Definition of Done per Task
Setiap task Codex dianggap selesai hanya jika:
- kode berjalan di staging,
- test case terkait lulus,
- demo singkat tersedia,
- log perubahan diperbarui,
- tidak merusak flow sebelumnya,
- acceptance owner terpenuhi.

## 16.7 Release Gate
### Gate 1 — Config Ready
Master data, role, environment, access sudah benar.

### Gate 2 — Process Ready
Flow transaksi end-to-end lulus pada staging.

### Gate 3 — Data Trust Ready
Dashboard dan laporan sudah direkonsiliasi dengan transaksi sumber.

### Gate 4 — UAT Ready
User bisnis menyetujui skenario utama.

## 17. Task Breakdown Template untuk Codex
Setiap task yang dikirim ke Codex sebaiknya konsisten memakai format berikut:

### Template Task
- Objective
- Scope
- Files/modules impacted
- Functional rules
- Acceptance criteria
- Test cases
- Out of scope
- Rollback note

### Contoh
**Objective:** Tambahkan project code wajib pada stock issue.

**Scope:** stock.picking, stock.move, custom validation, project cost tagging.

**Functional rules:** setiap internal transfer ke WIP atau goods issue ke project harus mengandung project_id.

**Acceptance criteria:**
- issue tanpa project_id ditolak,
- issue dengan project_id berhasil,
- laporan material by project ter-update.

**Test cases:**
- TC-INV-001 issue valid
- TC-INV-002 issue tanpa project
- TC-INV-003 report update

**Out of scope:** barcode scanning.

## 18. Risiko Implementasi
- scope terlalu besar di awal,
- master data tidak siap,
- user ingin semua custom sekaligus,
- job costing dipaksakan sebelum transaksi disiplin,
- dashboard dibuat sebelum source data stabil,
- terlalu banyak bypass manual,
- tidak ada project code governance.

## 19. Mitigasi
- pakai fase ketat,
- wajibkan project code sejak awal,
- mulai dari proses inti,
- buat dashboard setelah transaksi sehat,
- lakukan UAT per domain,
- setiap custom harus punya owner bisnis.

## 20. Rekomendasi Praktis untuk Eksekusi
1. Mulai dari **Odoo Community v17** agar lebih stabil untuk custom-heavy implementation.
2. Pisahkan custom module per domain, jangan satu modul raksasa.
3. Bangun **traceability matrix** sejak hari pertama.
4. Jadikan **staging demo mingguan** sebagai ritual wajib.
5. Dashboard direksi baru dianggap valid setelah rekonsiliasi data lulus.
6. Jangan mulai dari KPI; mulai dari disiplin transaksi.

## 21. Lampiran — Daftar KPI Inti dan Rumus
### Quote Win Rate
won quotation / total submitted quotation

### Material Readiness
available required material / total required material

### Work Order Completion Rate
completed WO / total released WO

### Labor Efficiency
standard hours / actual hours

### Rework Rate
rework hours / total production hours

### Gross Margin %
(revenue - actual cost) / revenue

### Vendor On-Time Delivery
on-time receipts / total receipts

### Inventory Accuracy
matched counted qty / total counted qty

### NCR Aging
hari terbuka sejak NCR dibuat sampai closed

### MTBF
total operating time / number of failures

### MTTR
total repair time / number of repairs

## 22. Kesimpulan
PRD ini dirancang agar dapat langsung dipakai sebagai panduan kerja Codex untuk membangun ERP heavy fabrication bertahap. Prinsip utamanya adalah: **mulai dari transaksi inti, paksa disiplin data, validasi setiap requirement lewat testable acceptance criteria, lalu naikkan kompleksitas hanya setelah data source terbuk