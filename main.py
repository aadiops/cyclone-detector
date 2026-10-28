from cyclone_detector import CycloneDetector


def main():
    import argparse
    import csv
    from pathlib import Path

    parser = argparse.ArgumentParser(description="Cyclone detector CLI")
    parser.add_argument("--file", type=str, help="CSV file containing weather observations")
    args = parser.parse_args()

    file_path = Path(args.file) if args.file else Path("sample_data.csv")

    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    detector = CycloneDetector()
    with file_path.open(newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    results = detector.analyze_records(rows)
    print("timestamp,wind_kmh,pressure_hpa,rainfall_mm,sea_temp_c,risk_score,status")
    for row in results:
        print(
            f"{row['timestamp']},{row['wind_kmh']},{row['pressure_hpa']},{row['rainfall_mm']},{row['sea_temp_c']},"
            f"{row['risk_score']},{row['status']}"
        )


if __name__ == "__main__":
    main()
