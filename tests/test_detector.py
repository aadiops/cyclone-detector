from cyclone_detector import CycloneDetector


def test_low_risk_case():
    detector = CycloneDetector()
    score = detector.score_risk(25, 1010, 5, 27)
    assert score < 35
    assert detector.classify_risk(score) == "Low risk"


def test_warning_case():
    detector = CycloneDetector()
    score = detector.score_risk(95, 970, 35, 30)
    assert score >= 80
    assert detector.classify_risk(score) == "Cyclone warning"


def test_batch_analysis():
    detector = CycloneDetector()
    records = [
        {"timestamp": "2026-10-01T00:00Z", "wind_kmh": 90, "pressure_hpa": 980, "rainfall_mm": 28, "sea_temp_c": 29.5},
        {"timestamp": "2026-10-01T06:00Z", "wind_kmh": 62, "pressure_hpa": 995, "rainfall_mm": 17, "sea_temp_c": 28.1},
    ]

    results = detector.analyze_records(records)
    assert len(results) == 2
    assert results[0]["status"] == "Cyclone warning"
    assert results[1]["status"] == "Cyclone watch"
