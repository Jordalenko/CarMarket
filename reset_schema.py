#!/usr/bin/env python
import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CarMarket.settings')
sys.path.insert(0, '/Users/sp3_mbp/Dropbox/CodeInstitute/PP4_02/CarMarket')

django.setup()

from django.db import connection

try:
    with connection.cursor() as cursor:
        print("Dropping public schema...")
        cursor.execute('DROP SCHEMA public CASCADE')
        print("Creating new public schema...")
        cursor.execute('CREATE SCHEMA public')
        print("Granting permissions...")
        cursor.execute('GRANT ALL ON SCHEMA public TO public')
    print("Schema reset complete")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
