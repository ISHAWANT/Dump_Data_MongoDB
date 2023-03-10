import pymongo 

import pandas as pd 
import json 


clinet = pymongo.MongoClient("mongoDB_Atlas_url") 

DATA_FILE_PATH = (r"C:\Users\ishaw\OneDrive\Desktop\insurance.csv")

DATABASE_NAME="INSURANCE" 
COLLECTION_NAME = 'INSURANCE_PROJECT' 

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"rows and columns: {df.shape}")

    df.reset_index(drop=True,inplace=True) 

    json_record = list(json.loads(df.T.to_json()).values())

    print(json_record[0])

    clinet[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)


