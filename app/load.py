from app.db import get_connection
from app.logger import logger

def load_to_mysql(data):
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO cart_details 
        (cart_id, product_id, title, price, quantity, total, discountPercentage, discountedPrice)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        for row in data:
            cursor.execute(query, tuple(row.values()))

        conn.commit()
        logger.info("Data loaded into MySQL")

    except Exception as e:
        logger.error(f"Load failed: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()