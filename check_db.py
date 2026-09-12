import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()
from account.models import Service
print("Services:")
for s in Service.objects.all():
    print(f"- {s.slug}: show_on_homepage={s.show_on_homepage}, sort_order={s.sort_order}")
import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    port=5433,
    user="diracai",
    password="1234",
    dbname="myproject",
)

cur = conn.cursor()

cur.execute("SELECT current_database(), current_user")
print("DATABASE:", cur.fetchone())

cur.execute("""
    SELECT tablename
    FROM pg_tables
    WHERE schemaname = 'public'
    ORDER BY tablename
""")

print("\nTABLES:")
for row in cur.fetchall():
    print(row[0])

conn.close()