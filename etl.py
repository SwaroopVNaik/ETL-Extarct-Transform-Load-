import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from app.extract import extract_data
from app.transform import transform_data
from app.load import load_to_mysql
from app.export import export_to_json

def run_pipeline():
    data = extract_data()

    if not data:
        return

    transformed = transform_data(data)

    if not transformed:
        return

    load_to_mysql(transformed)
    export_to_json()

if __name__ == "__main__":
    run_pipeline()