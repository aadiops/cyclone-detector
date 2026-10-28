# Cyclone Detector

A lightweight cyclone risk detection starter for evaluating storm conditions from observation data.

## Features

- Risk scoring from wind speed, pressure, rainfall, and sea temperature
- Batch analysis for multiple storm observations
- CSV input support for quick evaluation
- Simple CLI for local testing

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py --file sample_data.csv
```

## Example output

```text
timestamp,wind_kmh,pressure_hpa,rainfall_mm,sea_temp_c,risk_score,status
2026-10-01T00:00Z,90,980,28,29.5,83.0,Cyclone warning
2026-10-01T06:00Z,62,995,17,28.1,52.0,Cyclone watch
```

## Risk bands

- 0-34: Low risk
- 35-59: Monitor
- 60-79: Cyclone watch
- 80+: Cyclone warning
