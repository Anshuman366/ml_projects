from sklearn.pipeline import Pipeline
from sympy import im
from housing.pipeline.pipeline import pipeline
from housing.logger import logging
from housing.config.configuration import configuration
from housing.component.data_transformation import DataTransformation

def main():
    try:
        #logging.info("Pipeline stsrts")
        Pipeline=pipeline()
        Pipeline.run_pipeline()
        #config=configuration()
        #data_transformation_config=config.get_data_transformation_config()
        #print(data_transformation_config)
        #schema_file_path=r"C:\Users\prana\machine_learning_project_1\ml_projects\config\schema.yaml"
        #file_path=r"C:\Users\prana\machine_learning_project_1\ml_projects\housing\artifact\data_ingestion\2022-07-06_16-17-02\ingested_data\train\housing.csv"
       # df=DataTransformation.load_data(schema_file_path=schema_file_path,file_path=file_path)
        #print(df.columns)
        #print(df.dtypes)
    except Exception as e:
        print(e)

if __name__=="__main__":
    main()