from ast import Pass
from sympy import EX
from housing.entity.config_entity import *
from housing.util.util import read_yaml
from housing.constants import *
from housing.exception import Housing_exception
from housing.logger import logging

import sys

class configuration:
   
    def __init__(self,config_file_path:str=CONFIG_FILE_PATH, current_time_stamp:str=CURRENT_TIME_STAMP)->None:
        try:
                self.config_info=read_yaml(config_file_path) # return the yaml file in the form of dictionary that we have already seen in tje jupyter notebook
                self.training_pipeline_config=self.get_training_pipeline_config() # iski jarurat tab hogi jab hum artifact_dir k andar har ek component k artifat dir design kr rhe honge check data_ingestion_artifact_dir
                self.time_stamp=CURRENT_TIME_STAMP
        except Exception as e:
            raise Housing_exception(e,sys) from e
            
    def get_data_ingestion_config(self)->DataIngestionconfig:
        try:
            
            artifact_dir=self.training_pipeline_config.artifact_dir
            # This will give the outer artifact directort within this we can create our data_ingestion_artifact_dir
            
            data_ingestion_artifact_dir=os.path.join(artifact_dir,DATA_INGESTION_ARTIFACT_DIR,self.time_stamp)
            # This line will make The data_ingestion artifact directory within the main artifact folder
            
            
            data_ingestion_info=self.config_info[DATA_INGESTION_CONFIG_KEY] 
            ####This above line will contain the key of the data injection componenet (returned by the yaml file)
            
            dataset_download_url=data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY] 
            ###by using this we are getting the url information ,This is just a dictionary indexing by using various variable nothing else
            
            tgz_download_dir=os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY])
            ###This will create the tgz directory 
            
            raw_data_dir=os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY])
            ###This will create the raw data directory
            
            ingested_data_dir=os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY])
            # see this we are  creating a new folder ingested dir iske andar hum train and test csv ko rakhenge
            
            ingested_train_dir=os.path.join(artifact_dir,ingested_data_dir,data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY])   
            ## This will create a folder inside the ingested dir
            
            ingested_test_dir=os.path.join(artifact_dir,ingested_data_dir,data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY])
            ## this will also create a folder inside the ingestd dir folder
            
            
            data_ingestion_config=DataIngestionconfig(
                dataset_download_url=dataset_download_url, 
                tgz_download_dir=tgz_download_dir, 
                raw_data_dir=raw_data_dir, 
                ingested_train_dir=ingested_train_dir, 
                ingested_test_dir=ingested_test_dir
            )
            return data_ingestion_config
            logging.info(f"data_ingestion_config : {data_ingestion_config}")
        except Exception as e:
            raise Housing_exception(e,sys) from e
    
    def get_data_validation_config(self)->DataValidationconfig:
        try:
            
                schema_file_path=None
                data_validation_config=DataValidationconfig(schema_file_path=schema_file_path)
                return data_validation_config 
        except Exception as e:
            raise Housing_exception(e,sys) from e
            
    
    
    
    def get_data_transformation_config(self)->DataTransformationconfig:
        pass
    def get_model_trainer_config(self)->ModelTrainingconfig:
        pass
    def get_model_evaluation_config(self)->ModelEvaluation:
        pass
    def model_pusher_config(self)->ModelPusherconfig:
        pass
    def get_training_pipeline_config(self)->TrainingPipelineconfig:
        try:
            training_pipeline_config=self.config_info[TRAINING_PIPELINE_CONFIG_KEY] # This will return the key of the pipeline , jo yaml file k andar hai
            artifact_dir=os.path.join(ROOT_DIR,training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]) # This will join the root dir( that we have created inside the constant folder) and pipeline name and the artifact dir( which is TRAINING_PIPELINE_ARTIFACT_DIR from constant folder )
            training_pipeline_config=TrainingPipelineconfig(artifact_dir=artifact_dir) # name tuple return krega jisse ki jab hum training_pipeline_config return ko call kre class k through to wo sara info dede for this check the notebbok 
            logging.info(f"Training pipeling config: {training_pipeline_config}")
            return training_pipeline_config
            
        
        except Exception as e:
            raise Housing_exception(e,sys) from e 
            
        
        
        
        
        
#  so in this we can see that we have created the classes that will return the entity(yaml file ko read krenge aur jo structure tha entity ka usko input provide kr k return kr denge )
#  but yaml file ko read kaise krenge??? check the flow Txt FOCUS one thing ki ye configuration class 'koi function perform
#  nhi kr rha hai ye just folders k path ko setup kr rha hai 
        
        
        
