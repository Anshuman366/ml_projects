from collections import namedtuple

# in this folder jitni bhi chije required hai components ko usko define kis gya hai

DataIngestionconfig= namedtuple("DataIngestionconfig",["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])

DataValidationconfig=namedtuple("DataValidationconfig",["schema_file_path","report_file_path","report_page_file_path"])

DataTransformationconfig=namedtuple("DataTransformationconfig",["add_bedroom_per_room","tranformed_train_dir","transformed_test_dir","preprocessed_object_file_path"])

ModelTrainingconfig=namedtuple("ModelTrainingconfig",["trained_model_file_path","base_accuracy"])

ModelEvaluation=namedtuple("ModelEvaluation",["model_evaluation_file_path","time_stamp"])

ModelPusherconfig=namedtuple("ModelPusherconfig",["export_dir_path"])

TrainingPipelineconfig=namedtuple("TrainingPipelineconfig",["artifact_dir"])





# 1) schema_file_path->how many rows,columns are there in dataset and what are their datatype, The path of that file is located here
# 2) preprocessed_object_file_path-> the pickle file of the data transformation step will be stored at this location
# 3) tranformed_train_dir-> transformed data location
# 4) add_bedroom_per_room-> 
# 5) trained_model_file_path-> trained model should be saved somewhere that will be stored here
# 6) base_accuracy-> if my model is giving the accuracy better then this base accuracy then dont accept the model
# 7) model_evaluation_file_path-> suppose we have various models in the  production which have some accuracy so after finishig our model training we have to compare the accuracy of our model with the model which is already in the production
                                # so this file path will have  all the info about the models which is in production

# time_stamp -> at what time did we evaluate our model


#""" So This is just a structure it simply says that this many things are required by each component , The information 
#can be provided  by hard coding here only or we can provide the data from some other database ,suppose in mongodb i have stored
#the url of dataset and various file path  we can also read it from there for providing the data we will create a new folder outside the housing (config) and inside it we will create 
#a config.yaml file to provode the data"""
