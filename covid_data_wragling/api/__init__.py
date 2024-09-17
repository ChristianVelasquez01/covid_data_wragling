import pandas as pd
from sodapy import Socrata

def get_data(record_limit, department_name):
    client = Socrata("www.datos.gov.co", "eBREZAoYMbC9z3ky0vxQjxcB2")
    data = client.get("gt2j-8ykr", limit=record_limit, departamento_nom=department_name)
    
    return data

def process_data(data):
    data_frame = pd.DataFrame.from_records(data)

    return data_frame