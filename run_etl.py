from etl.extract import extract
from etl.transform import transform
from etl.load import load
from dotenv import load_dotenv
import os
from datetime import datetime

# Loading the environment variables
load_dotenv()

def run_etl():
    print(f'Running the ETL process at {datetime.now()}')
    TABLE_NAME = os.getenv('TABLE_NAME')
    
    data = extract('Berlin')
    data_frame = transform(data)
    load(data_frame,TABLE_NAME)

    print("ETL process is completed!!")


