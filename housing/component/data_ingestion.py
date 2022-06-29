from housing.config.configuration import configuration
from housing.entity.config_entity import DataIngestionconfig
from housing.exception import Housing_exception
from housing.logger import logging
import sys,os
from housing.entity.artifact_entity import DataIngestionArtifact
import tarfile  # Python tarfile module is used to read and write tar archives.
from six.moves import urllib
class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionconfig):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise Housing_exception(e,sys) from e #from e likhne ka matlab ye hai ki jab hume exception aaiga to usme ye na show ho ki wo isi line se exception raise hua hai wo actual jha se exception raise hua hai wha point kre 
        
        
    def download_housing_data(self):
        try:
            ## accessing the url to download the content
            download_url=self.data_ingestion_config.dataset_download_url
            
            ## Extracting the tgz download directory that we have already created in out config.configuration file
            tgz_download_dir=self.data_ingestion_config.tgz_download_dir
            
        
                
            ## Now focus that the tgz_download_dir is not available now because in component we just have created the path we 
            ## have not created any kind of folder , folder creation will be done in this section 
            ## But there is also one thing that of tgz_download_dir exist but what if it contain a unuseful thing for us
            ## to solve this we will delete that file and then again create it 
            
            if os.path.exists(tgz_download_dir):
                os.remove(tgz_download_dir)
                
            os.makedirs(tgz_download_dir,exist_ok=True) # now we will crete the folder freshly
            
            # we are creating a housing_file_name which we are extracting from the download_url 
            # There is a method in os modeule which will give the name of the file from the url 
            # we can also use the url.split("/")[-1] this will also work
            housing_file_name=os.path.basename(download_url)
            
            # see dont get confused when u see this, because in configuration we just have created the root directory now 
            # we will go inside that and will create the actual functioning for this we will create a file in tgz download dir
            
            tgz_file_path=os.path.join(tgz_download_dir,housing_file_name) # this is the place where we download oue tgz file
            
            logging.info(f"Downloading file from [{download_url}] at location [{tgz_file_path}]")
           
            urllib.request.urlretrieve(download_url,tgz_file_path)  #This will download the content of the url and will store inside the tgz_file_path
            logging.info(f"Downloading completed sucessfully at location : [{tgz_file_path}]")
            
            # now as we have downloaded the file  at tgz_file_path we can return that path
            return tgz_file_path   
            
        except Exception as e:
            raise Housing_exception(e,sys) from e
        
        
    def extract_tgz_file(self,tgz_file_path):
        """ This will take a parameter tgz_file_path and try to extract  the data into the raw_data_dir"""
        try:
            raw_data_dir=self.data_ingestion_config.raw_data_dir # This will give the raw_data_dir where er hsve to store the Extracted data
            
            # it will check the same thing as in above method
            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)
                
            os.makedirs(raw_data_dir,exist_ok=True)
            
            
            logging.info(f"Extracting tgz file: [{tgz_file_path}] into dir [{raw_data_dir}]")
            # NOW WE WILL EXTRACT THE FILE AND THEN WE WILL STORE IN THE raw_data_dir FOR THIS WE WILL USE  THE TARFILE MODULE 
            with tarfile.open(tgz_file_path) as housing_tgz_file_object:
                housing_tgz_file_object.extractall(path=raw_data_dir) # in this we are extracting the data and storing it into the raw_data_dir
            logging.info(f"Extraction completed!!!")
            
        except Exception as e:
            raise Housing_exception(e,sys) from e
    
    def split_data_as_train_test(self):
        """ This function will give -> DataIngestionArtifact as output because this will \
            provode train and test data to the data validation component"""
        try:
            raw_data_dir=self.data_ingestion_config.raw_data_dir
            
            
            
        except Exception as e:
            raise Housing_exception(e,sys) from e
        
    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try: 
            tgz_file_path=self.download_housing_data() # This class will return the file path see above code
            self.extract_tgz_file(tgz_file_path=tgz_file_path) # here we are just passing the parameter to the extract_tgz_file() class
        except Exception as e:
            raise Housing_exception(e,sys) from e
        
   