import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "custom_sql_agent"

list_of_files = [
    "artifacts/vector_db/.gitkeep",
    "artifacts/sqlite_db/.gitkeep",
    "artifacts/summaries/.gitkeep",
    "artifacts/outputs/.gitkeep",
    "artifacts/results/.gitkeep",

    "notebooks/01_minimal_agent.ipynb",
    "notebooks/02_custom_agent.ipynb",

    # pipeline
    "rag_pipeline/__init__.py",
    "rag_pipeline/stage_01.py",
    "rag_pipeline/stage_02.py",
    "rag_pipeline/stage_03.py",

    # utils
    "utils/__init__.py",
    "utils/config.py",
    "utils/logger.py",
    "utils/server.py",
    
    "utils/helpers/__init__.py",
    "utils/workflow/__init__.py",
    
    "utils/llm/__init__.py",
    "utils/llm/prompt_temp.py",
    "utils/llm/llm_func.py",

    # main
    # "main.py",
    "app.py",

    # tests
    "tests/__init__.py",
    
    # docs
    "docs/README.md",
    "docs/REFERENCE.md",
    "docs/ARCHITECTURE.md",
    "docs/INSTALLATION.md",
    "docs/CONTRIBUTING.md",

    "params.yaml",
    "dvc.yaml",
    ".env.local",
    ".env.example",
]


for filepath in list_of_files:
    filepath = Path(filepath) #to solve the windows path issue
    filedir, filename = os.path.split(filepath) # to handle the project_name folder


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")