import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO,format='[%(ascitime)s]: %(message):')

project_name="animal classifier"

list_directory=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]


for filePath in list_directory:
    #converting the path to the current operating system
    filePath=Path(filePath)
    #separating directory and file name
    #all folders and  the end files
    filedir,filename=os.path.split(filePath)

    #if the file directory is not empty
    if filedir!="":
        #creating directory
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory;{filedir} for the file: {filename}")
    #if the path doesn't exist or the file doesn't contain any code
    #we create a new empty file
    if (not os.path.exists(filePath)) or (os.path.getsize(filePath)==0):
        with open(filePath,'w') as f:
            pass
            logging.info(f"Creating empty file:{filePath}")

    else:
        logging.info(f"{filename} already exists")