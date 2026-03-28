import requests
import mysql.connector
import json

# ✅ Extract Function
def extract_data():
    url = "https://dummyjson.com/carts"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("✅ Data Extracted Successfully")
        return data
    else:
        print("❌ Failed to fetch data")
        return None


# ✅ Transform Function
def transform_data(data):
    transformed = []

    for cart in data["carts"]:
        cart_id = cart["id"]

        for product in cart["products"]:
            row = {
                "cart_id": cart_id,
                "product_id": product["id"],
                "title": product["title"],
                "price": product["price"],
                "quantity": product["quantity"],
                "total": product["total"],
                "discountPercentage": product["discountPercentage"],
                "discountedPrice": product["discountedTotal"]
            }

            transformed.append(row)

    print("✅ Data Transformed Successfully")
    return transformed

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="rzbkpdr74h",  # 👈 CHnage this according to your workbench password
        database="etl_db"
    )
    
def load_to_mysql(data):
    conn = connect_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO cart_details 
    (cart_id, product_id, title, price, quantity, total, discountPercentage, discountedPrice)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    for row in data:
        values = (
            row["cart_id"],
            row["product_id"],
            row["title"],
            row["price"],
            row["quantity"],
            row["total"],
            row["discountPercentage"],
            row["discountedPrice"]
        )
        cursor.execute(query, values)

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ Data Loaded into MySQL")

def export_to_json():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)  # 🔥 important

    query = "SELECT * FROM cart_details"
    cursor.execute(query)

    rows = cursor.fetchall()

    # Write to JSON file
    with open("carts_data.json", "w") as f:
        json.dump(rows, f, indent=4)

    cursor.close()
    conn.close()

    print("✅ Data Exported to JSON")

if __name__ == "__main__":
    data = extract_data()
    
    if data:
        transformed_data = transform_data(data) # Transforming Json to MYSQL
        load_to_mysql(transformed_data) # loading data 
        export_to_json() # exporting data from Mysql to JSON