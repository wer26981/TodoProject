from pathlib import Path
from .models import Todo
from dataclasses import asdict,dataclass
import json
DATA_FILE = Path("data/todos.json")

class TodoStorage:

    def __init__(self,path:Path=DATA_FILE)->None:
        self.path=path

    def load(self)->list[Todo]:
        if not self.path.exists():
            return []
        with self.path.open("r",encoding="utf-8") as f:
            data = json.load(f)
        return [Todo(**item) for item in data] #**代表将字典转化为列表
    
    def save(self,todos:list[Todo])->None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w",encoding="utf-8") as f:
            json.dump([asdict(s) for s in todos],f,ensure_ascii=False,indent=2, default=str)