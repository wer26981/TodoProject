from dataclasses import dataclass 
from typing import Optional
@dataclass
class Todo:
    id:int
    name:str
    completed:bool = False
    description:Optional[str] = None