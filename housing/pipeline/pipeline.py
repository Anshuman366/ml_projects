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
       
    def start_data_ingestion():
        """ This function will return the DataIngestionArtifact"""
        try:
            data_ingestion = DataIngestion(data_ingestion_config= self.c)
        except Exception as e:
            raise Housing_exception(e,sys) from e