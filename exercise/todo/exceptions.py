class TodoException(Exception):
    pass


class TodoNotFoundException(TodoException):
    def __init__(self, todo_id: int):
        super().__init__(f"没有找到id={todo_id}的todo事项")
        self.todo_id = todo_id
