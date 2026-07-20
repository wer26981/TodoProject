from dataclasses import dataclass 
@dataclass
class Todo:
    id:int
    name:str
    complect:bool = False