from __future__ import annotations

from typing import Dict, Iterable, List


class CycloneDetector:
    def score_risk(self, wind_kmh: float, pressure_hpa: float, rainfall_mm: float, sea_temp_c: float) -> float:
        """Return a normalized cyclone risk score between 0 and 100."""
        wind_component = min(50.0, max(0.0, wind_kmh / 2.0))
        pressure_component = min(30.0, max(0.0, (1013.0 - pressure_hpa) / 5.0))
        rainfall_component = min(15.0, max(0.0, rainfall_mm / 4.0))
        sea_temp_component = min(10.0, max(0.0, (sea_temp_c - 26.0) * 3.0))

        risk_score = wind_component + pressure_component + rainfall_component + sea_temp_component
        return round(min(100.0, risk_score), 1)

    def classify_risk(self, risk_score: float) -> str:
        if risk_score < 35:
            return "Low risk"
        if risk_score < 60:
            return "Monitor"
        if risk_score < 80:
            return "Cyclone watch"
        return "Cyclone warning"

    def analyze_records(self, records: Iterable[Dict[str, str]]) -> List[Dict[str, float | str]]:
        results: List[Dict[str, float | str]] = []
        for record in records:
            wind_kmh = float(record.get("wind_kmh", 0))
            pressure_hpa = float(record.get("pressure_hpa", 1013))
            rainfall_mm = float(record.get("rainfall_mm", 0))
            sea_temp_c = float(record.get("sea_temp_c", 26))
            timestamp = record.get("timestamp", "unknown")

            risk_score = self.score_risk(wind_kmh, pressure_hpa, rainfall_mm, sea_temp_c)
            status = self.classify_risk(risk_score)

            results.append(
                {
                    "timestamp": timestamp,
                    "wind_kmh": wind_kmh,
                    "pressure_hpa": pressure_hpa,
                    "rainfall_mm": rainfall_mm,
                    "sea_temp_c": sea_temp_c,
                    "risk_score": risk_score,
                    "status": status,
                }
            )

        return results
