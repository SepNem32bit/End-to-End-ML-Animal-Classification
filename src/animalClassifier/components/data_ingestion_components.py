import os
import urllib.request as request
from zipfile import ZipFile
from tqdm import tqdm
from pathlib import Path
from src.animalClassifier.entity import DataIngestionConfig
from src.animalClassifier.utils import get_size
from src.animalClassifier import logger

#we extract and retrieve the jpeg data from zip folder

class DataIngestion:
    #we will use the output format config
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info("Trying to download file...")
        if not os.path.exists(self.config.local_data_file):
            logger.info("Download started...")
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}") 

    #when we have _ before the method's name, it makes it hidden and inaccessible
    def _get_updated_list_of_files(self, list_of_files):
        #only jpeg files are listed 
        return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)]
    

    #Extract File from ZIP and check for empty files
    def _extractCheck(self, zf: ZipFile, working_dir: str, f: str):
        # Define the target file path where the file should be extracted
        target_filepath = os.path.join(working_dir, f)
        #This ensures that files are not extracted multiple times if they already exist in the target directory.
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir) 
        # If the file is empty, delete it  
        if os.path.getsize(target_filepath) == 0:
            os.remove(target_filepath)


    def unzip_and_clean(self):
        #local data file defined in config where download file is 
        with ZipFile(file=self.config.local_data_file, mode="r") as zf:
            # Get the list of files and folders in the zip archive
            list_of_files = zf.namelist()
            #filter based on only jpeg images
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)
            #tqdm(updated_list_of_files) wraps the loop, displaying a real-time progress bar in the console as the files are processed
            for f in tqdm(updated_list_of_files):
                self._extractCheck(zf, self.config.unzip_dir,f)