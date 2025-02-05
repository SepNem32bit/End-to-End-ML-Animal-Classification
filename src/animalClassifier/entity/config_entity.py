from dataclasses import dataclass
from pathlib import Path

#returning all config parameters which will be used in arrow function output entities
#@dataclass(frozen=True) is a decorator in Python's dataclasses module that makes instances of the class immutable after creation. 
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path