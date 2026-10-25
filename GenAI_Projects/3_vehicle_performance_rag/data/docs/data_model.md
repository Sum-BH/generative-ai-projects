# Data Model Overview

The data model follows a star-like structure optimized for BI tools.

---

## Core Tables

### telemetry_operating_profile
- rpm_bin_low
- rpm_bin_high
- load_bin_low
- load_bin_high
- time_spent
- source_file

---

### telemetry_thermal_behavior
- timestamp
- oil_temperature
- coolant_temperature
- overshoot_flags
- source_file

---

### telemetry_environmental_profile
- grade_pct
- source_file

---

### telemetry_actuation_statistics
- event_counts
- state_mismatch_counts
- distance_normalized_metrics
- source_file

---

### telemetry_frequency_features
- fft_energy
- dominant_frequencies
- source_file

---

## Keys & Relationships

- `source_file` acts as a logical partition key
- Tables are intentionally denormalized for BI performance
