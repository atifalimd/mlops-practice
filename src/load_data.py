# read te data from data source
# save it in the data/raw

import os
from get_data import read_params, get_data
# instea of getting data from the cloud, fetching data from the get_data folder
import argparse

def load_save(config_path): #importing config and data from the get_data file
    config = read_params(config_path)
    df = get_data(config_path)
    new_cols = [col.replace(' ','_') for col in df.columns]
    raw_data_path = config['load_data']["raw_dataset_csv"]
    df.to_csv(raw_data_path, sep =',', index = False, header=new_cols)



if __name__ =="__main__":
    args = argparse.ArgumentParser() ## import class
    args.add_argument("--config",default = "params.yaml") 
    parsed_args = args.parse_args()
    
    data = load_save(config_path = parsed_args.config)
