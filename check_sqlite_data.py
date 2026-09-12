import sqlite3

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

tables = [
    "account_account",
    "account_employeeprofile",
    "account_project",
]

for table in tables:
    try:
        cursor.execute(f'SELECT COUNT(*) FROM "{table}"')
        count = cursor.fetchone()[0]
        print(f"{table}: {count}")
    except Exception as e:
        print(f"{table}: ERROR - {e}")

print("\nEmployee sample:")
try:
    cursor.execute("""
        SELECT id, employee_id
        FROM account_employeeprofile
        LIMIT 10
    """)
    for row in cursor.fetchall():
        print(row)
except Exception as e:
    print("Employee sample error:", e)

print("\nProject sample:")
try:
    cursor.execute("""
        SELECT id, name
        FROM account_project
        LIMIT 10
    """)
    for row in cursor.fetchall():
        print(row)
except Exception as e:
    print("Project sample error:", e)

conn.close()