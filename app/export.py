import json
from app.db import get_connection
from app.logger import logger

def export_to_json():
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM cart_details")
        data = cursor.fetchall()

        with open("carts_data.json", "w") as f:
            json.dump(data, f, indent=4)

        logger.info("Data exported to JSON")

    except Exception as e:
        logger.error(f"Export failed: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()