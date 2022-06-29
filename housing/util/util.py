import yaml
from housing.exception import Housing_exception
import os,sys

def read_yaml(file_path:str)->dict:
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise Housing_exception(e,sys) from e
    
