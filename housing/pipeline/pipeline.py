import imp
from numpy import RAISE
from housing.component import data_ingestion
from housing.component.data_validation import DataValidation
from  housing.config.configuration import configuration
from housing.logger import logging
from housing.exception import Housing_exception
from housing.entity.artifact_entity import DataValidationArtifact


from housing.entity.config_entity import DataIngestionconfig
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.component.data_ingestion import DataIngestion
from housing.component.data_validation import DataValidation
from housing.component.data_transformation import DataTransformation
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
        
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact):
        """ This will return the DataValidationArtifact"""
        try:
            data_validation=DataValidation(data_validation_config=self.config.get_data_validation_config(),data_ingestion_artifact=data_ingestion_artifact)
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise Housing_exception(e,sys) from e
            

            
            
    def start_data_transformation(self,
                                  data_ingestion_artifact: DataIngestionArtifact,
                                  data_validation_artifact: DataValidationArtifact
                                  ):
        try:
            data_transformation = DataTransformation(
                data_transformation_config=self.config.get_data_transformation_config(),
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_artifact=data_validation_artifact
            )
            return data_transformation.initiate_data_transformation()
        except Exception as e:
            raise Housing_exception(e, sys) from e


    def start_model_trainer(self):
        pass

    def start_model_evaluation(self):
        pass

    def start_model_pusher(self):
        pass
    
    def run_pipeline(self):
        try:
            
            data_ingestion_artifact=self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact=self.start_data_transformation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_artifact=data_validation_artifact)
            
        except Exception as e:
            raise Housing_exception(e,sys) from e