# Analytics Architecture

The system follows a layered telemetry analytics architecture:

1. Data Generation / Ingestion  
2. Signal Cleaning & Normalization  
3. Modular Analytics Processing  
4. SQL Persistence  
5. BI Visualization

---

## Architecture Flow

Telemetry Sources
↓
Ingestion & Normalization
↓
Processed Telemetry Store
↓
Analytics Modules
↓
Relational Database (SQL)
↓
Power BI Dashboards

## Architechture - Detailed

┌────────────────────────────┐
│   Telemetry Sources        │
│  (Logs / Sensors / CSV)   │
└──────────────┬────────────┘
               │
               ▼
┌────────────────────────────┐
│   Ingestion & Normalization│
│  - Timestamp alignment     │
│  - Signal cleaning         │
│  - Plausibility checks     │
└──────────────┬────────────┘
               │
               ▼
┌────────────────────────────┐
│   Processed Telemetry      │
│  (Analytics-ready signals) │
└──────────────┬────────────┘
               │
               ▼
┌──────────────────────────────────────────┐
│   Modular Analytics Layer                 │
│                                          │
│  ┌────────────────────────────────────┐  │
│  │ Operating Profile Analytics         │  │
│  ├────────────────────────────────────┤  │
│  │ Thermal Behavior Analytics          │  │
│  ├────────────────────────────────────┤  │
│  │ Environmental Profile Analytics     │  │
│  ├────────────────────────────────────┤  │
│  │ Actuation & State Transition Stats  │  │
│  ├────────────────────────────────────┤  │
│  │ Frequency-Domain (FFT) Analytics    │  │
│  └────────────────────────────────────┘  │
└──────────────┬───────────────────────────┘
               │
               ▼
┌────────────────────────────┐
│   Relational Database      │
│  (BI-friendly tables)     │
└──────────────┬────────────┘
               │
               ▼
┌────────────────────────────┐
│   Power BI Dashboards      │
│  - Interactive slicing    │
│  - Refreshable insights   │
└────────────────────────────┘

---

## Design Principles

- Modularity: each analytics module is independent
- Traceability: raw, processed, and analytics datasets are separated
- Scalability: processing logic supports multiple assets/files
- BI-first outputs: tables are shaped for direct visualization
- Reproducibility: deterministic synthetic data generation

---

## Analytics Isolation

Each analytics question:
- Uses only required signals
- Produces its own output table
- Can be enabled/disabled independently

This mirrors real-world engineering analytics programs.
