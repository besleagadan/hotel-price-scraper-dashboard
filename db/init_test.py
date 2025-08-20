from db.connect import get_connection


def insert_test():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO hotels (name, location, date, price, source) VALUES (%s, %s, %s, %s, %s)",
        ("Test Hotel", "Paris", "2025-08-19", 120.50, "Booking.com")
    )

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    insert_test()
    print("✅ Test row inserted")
