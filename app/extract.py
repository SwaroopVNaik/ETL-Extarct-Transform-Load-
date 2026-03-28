import requests
from app.logger import logger

def extract_data():
    try:
        url = "https://dummyjson.com/carts"
        response = requests.get(url)

        response.raise_for_status()

        logger.info("Data extracted successfully")
        return response.json()

    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        return None