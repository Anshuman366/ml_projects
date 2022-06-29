from housing.config.configuration import configuration
from housing.entity.config_entity import DataIngestionconfig
from housing.exception import Housing_exception
import sys,os
from housing.entity.artifact_entity import DataIngestionArtifact

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionconfig):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise Housing_exception(e,sys) from e
        
    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try: 
            pass
        except Exception as e:
            raise Housing_exception(e,sys) from e