import csv
import json
import os
import sys
from pathlib import Path
import django

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CarMarket.settings")
django.setup()

from users.models import Profile

csv_file = BASE_DIR / "listings" / "fixtures" / "Cars_Datasets_2026_v2_with_ids.csv"
json_file = BASE_DIR / "listings" / "fixtures" / "Cars_Datasets_2026_v2.json"
profile_fixture = BASE_DIR / "listings" / "fixtures" / "profile.json"

data = []
profile_username_to_id = {}

if profile_fixture.exists():
    with open(profile_fixture, encoding="latin-1") as f:
        profile_data = json.load(f)

    for entry in profile_data:
        fields = entry.get("fields", {})
        username = (fields.get("username") or "").strip().lower()
        if username:
            profile_username_to_id[username] = str(entry.get("pk"))

with open(csv_file, newline="", encoding="latin-1") as f:
    reader = csv.DictReader(f)

    for row in reader:
        owner_key = (row.get("owner_id") or "").strip()
        owner_id = None

        if owner_key:
            owner_id = profile_username_to_id.get(owner_key.lower())
            if not owner_id:
                owner_profile = Profile.objects.filter(username__iexact=owner_key).first()
                owner_id = str(owner_profile.id) if owner_profile else None

        item = {
            "model": "listings.listing",
            "pk": row["id"].strip() if row["id"] else None,
            "fields": {
                "owner": owner_id,
                "car_make": int(row["car_make_id"]) if row["car_make_id"] else None,
                "car_model": int(row["car_model_id"]) if row["car_model_id"] else None,
                "mileage": int(row["mileage"]) if row["mileage"] else None,
                "year": int(row["year"]) if row["year"] else None,
                "engine_size": row["engine_size"].strip() if row["engine_size"] else "",
                "transmission": row["transmission"].strip() if row["transmission"] else "",
                "created": row["created"].strip() if row["created"] else None,
                "description": row["description"].strip() if row["description"] else "",
                "price": int(row["price"]) if row["price"] else None,
                "fuel_type": row["fuel_type"].strip() if row["fuel_type"] else "",
                "seats": int(row["seats"]) if row["seats"] else None,
                "torque": int(row["torque"]) if row["torque"] else None,
                "listing_image_1": row["images"].strip() if row["images"] else "listings/default-listing-img.jpg"
            }
        }
        data.append(item)

with open(json_file, "w", encoding="latin-1") as f:
    json.dump(data, f, indent=2)

print("Cars_Datasets_2026_v2.json fixture created successfully")
