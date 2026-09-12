import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from django.db import connection

print("Database:", connection.settings_dict["NAME"])
print("Port:", connection.settings_dict["PORT"])

with connection.cursor() as cursor:
    tables_to_check = [
        "account_account",
        "account_employeeprofile",
        "account_project",
        "account_employeeticket",
    ]

    print("\n--- TABLE CHECK ---")

    for table in tables_to_check:
        try:
            cursor.execute(f'SELECT COUNT(*) FROM "{table}"')
            count = cursor.fetchone()[0]
            print(f"{table}: {count}")
        except Exception as e:
            print(f"{table}: ERROR - {e}")

    print("\n--- ACCOUNT SAMPLE ---")
    try:
        cursor.execute("""
            SELECT id, username, email
            FROM account_account
            LIMIT 10
        """)
        for row in cursor.fetchall():
            print(row)
    except Exception as e:
        print("Account sample error:", e)

    print("\n--- PROJECT COLUMNS ---")
    try:
        cursor.execute("""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = 'account_project'
            ORDER BY ordinal_position
        """)
        for row in cursor.fetchall():
            print(row[0])
    except Exception as e:
        print("Project columns error:", e)