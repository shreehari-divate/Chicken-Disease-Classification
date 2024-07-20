import os
from pathlib import Path
import logging

#creating a logging message
logging.basicConfig(level=logging.INFO, format='[%(ascitime)s]: %(message)s')

#defining the project name:
project_name='ChickenDiseaseClassifier'

#listing the file/folders to be created
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/confiuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)

    if filedir !="": #to check if directory is not empty and create a directory if it does not exists
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory; {filedir} for the file: {filename}")

    #to check if file does not exists or is empty, if so, create an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):   
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")        