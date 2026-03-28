from app.logger import logger

def transform_data(data):
    try:
        transformed = []

        for cart in data["carts"]:
            for product in cart["products"]:
                transformed.append({
                    "cart_id": cart["id"],
                    "product_id": product["id"],
                    "title": product["title"],
                    "price": product["price"],
                    "quantity": product["quantity"],
                    "total": product["total"],
                    "discountPercentage": product["discountPercentage"],
                    "discountedPrice": product["discountedTotal"]
                })

        logger.info("Data transformed successfully")
        return transformed

    except Exception as e:
        logger.error(f"Transformation failed: {e}")
        return []