from dataclasses import dataclass
#from data import data
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tool import tool

@dataclass
class to_do_class:
    name_task: str 
    descri_task:str
    timer : int
    state : bool
