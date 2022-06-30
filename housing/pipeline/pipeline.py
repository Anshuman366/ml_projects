from housing.component import data_ingestion
from  housing.config.configuration import configuration
from housing.logger import logging
from housing.exception import Housing_exception

from housing.entity.config_entity import DataIngestionconfig
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.component.data_ingestion import DataIngestion
import os,sys



class pipeline:
    def __init__(self,config:configuration=configuration()) -> None:
       try:
           self.config=config
       except Exception as e:
           raise Housing_exception(e,sys) from e
       
    def start_data_ingestion(self):
        """ This function will return the DataIngestionArtifact"""
        try:
            data_ingestion = DataIngestion(data_ingestion_config= self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise Housing_exception(e,sys) from e
        
    def start_data_validation(self):
        pass

    def start_data_transformation(self):
        pass

    def start_model_trainer(self):
        pass

    def start_model_evaluation(self):
        pass

    def start_model_pusher(self):
        pass
    
    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.start_data_ingestion()
        except Exception as e:
            raise Housing_exception(e,sys) from e