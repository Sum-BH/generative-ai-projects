# Analytics Definitions

This project implements the following analytics modules:

---

## Operating Profile Analytics

Quantifies time spent across operating regions defined by:
- Load (e.g., torque)
- Speed (e.g., RPM)

Output:
- Time accumulation per operating bin
- Suitable for matrix and heatmap visuals

---

## Thermal Behavior Analytics

Monitors thermal signals against safe operating thresholds:
- Continuous temperature tracking
- Overshoot detection and counting

Used to identify:
- Sustained thermal stress
- Frequency of excursions

---

## Environmental Profile Analytics

Analyzes external or environmental signals:
- Grade / inclination
- Road or operating conditions

Used for:
- Distribution analysis
- Scenario comparison

---

## Actuation & State Transition Analytics

Tracks:
- Actuation events
- State mismatches
- Event frequency normalized by distance or time

Used to evaluate:
- Control behavior
- System stability

---

## Frequency-Domain Analytics

Applies FFT to vibration signals to extract:
- Total spectral energy
- Dominant frequencies

Used for:
- NVH assessment
- Early fault indicators
