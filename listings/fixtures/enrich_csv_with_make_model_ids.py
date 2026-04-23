import csv
import os
import sys
from pathlib import Path
import django

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CarMarket.settings")
django.setup()

from listings.models import CarMake, CarModel  # noqa: E402

input_csv = BASE_DIR / "listings" / "fixtures" / "Cars_Datasets_2026_v3.csv"
output_csv = BASE_DIR / "listings" / "fixtures" / "Cars_Datasets_2026_v3_with_ids.csv"

rows = []

with open(input_csv, newline="", encoding="latin-1") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames.copy()

    if "car_make_id" not in fieldnames:
        fieldnames.insert(fieldnames.index("car_make") + 1, "car_make_id")
    if "car_model_id" not in fieldnames:
        fieldnames.insert(fieldnames.index("car_model") + 1, "car_model_id")

    for row in reader:
        make_name = (row.get("car_make") or "").strip()
        model_name = (row.get("car_model") or "").strip()

        make_obj = CarMake.objects.filter(name__iexact=make_name).first()
        if make_name and not make_obj:
            make_obj = CarMake.objects.create(name=make_name)

        model_obj = None
        if make_obj:
            model_obj = CarModel.objects.filter(name__iexact=model_name, car_make=make_obj).first()
            if model_name and not model_obj:
                model_obj = CarModel.objects.create(name=model_name, car_make=make_obj)

        row["car_make_id"] = make_obj.id if make_obj else ""
        row["car_model_id"] = model_obj.id if model_obj else ""
        rows.append(row)

with open(output_csv, "w", newline="", encoding="latin-1") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Cars_Datasets_2026_v3_with_ids.csv created successfully")
