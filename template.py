import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format= '[%(asctime)s]: %(message)s:')

project_name = 'TextSummarizer'

## Creating multiple folders 
# The below list is created to make sure that our files will be automaticllay picked from github & deployed in cloud
# Initally the .github will be blank hence we created one more file .gitkeeps to make sure pushing happnes. later
    # we can delete this file
# __init__ is created to make sure that project_name become the local package henc we will be able to import anything
    # from project_name

list_of_files = [
    '.github/workflows/.gitkeeps',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
]


for filepath in list_of_files:
    filepath = Path(filepath) #This will detect the os and path to handle the issues with working in different OSes
    filedir, filename = os.path.split(filepath) #this is use to separate the foldername and filenames
    # but what if filedir is empty then?
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory {filedir} for file {filename}')
    
    # but what if filepath is not there? This is to make sure if there is some content in any file we will not 
        #overwrite it. insted we will create another file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'Creating empty file {filepath}')
    else:
        logging.info(f'{filepath} is already exists')
    


















