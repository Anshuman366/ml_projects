from sklearn.pipeline import Pipeline
from sympy import im
from housing.pipeline.pipeline import pipeline
from housing.logger import logging

def main():
    try:
        
        pipeline_run=pipeline()
        pipeline_run.run_pipeline
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__=="__main__":
    main()