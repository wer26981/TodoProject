from .models import Todo
from .storage import TodoStorage

class TodoServices:
    def __init__(self,storage:TodoStorage|None = None):
        self.storage=storage or TodoStorage()
        self.todos = self.storage.load()
    
    def _next_id(self)->int:
        return max((t.id for t in self.todos),default=0)+1
    
    def _index_of(self,todo_id:int)->int | None:
        for i,r in enumerate(self.todos):
            if r.id == todo_id:
                return i
        return None
        
        
    def add(self,name:str)->Todo:
        todo = Todo(self._next_id(),name)
        self.todos.append(todo)
        self.storage.save(self.todos)
        return todo
        

    def get(self,todo_id:int)->Todo|None:
        i = self._index_of(todo_id)
        if i == None:
            return None
        return self.todos[i]
    

    def list_all(self)->list[Todo]:
        return self.todos
    

    def update(self,todo_id:int,name:str|None=None,completed:bool|None=None)->Todo|None:
        i = self._index_of(todo_id)
        if i == None:
            return None
        t = self.todos[i]
        if not name == None:
            t.name=name
        if not completed == None:
            t.completed=completed
        self.storage.save(self.todos)
        return t
            
    def delete(self,todo_id:int)->bool:
        i = self._index_of(todo_id)
        if i == None:
            return False
        self.todos.pop(i)
        self.storage.save(self.todos)
        return True
    