import psycopg2

for port in [5432, 5433]:
    print(f"\n========== PORT {port} ==========")

    try:
        conn = psycopg2.connect(
            host="127.0.0.1",
            port=port,
            database="postgres",
            user="diracai",
            password="1234",
        )

        conn.autocommit = True
        cursor = conn.cursor()

        cursor.execute("""
            SELECT datname
            FROM pg_database
            WHERE datistemplate = false
            ORDER BY datname
        """)

        databases = [row[0] for row in cursor.fetchall()]

        print("Databases:")
        for db in databases:
            print(" -", db)

        cursor.close()
        conn.close()

    except Exception as e:
        print("ERROR:", e)