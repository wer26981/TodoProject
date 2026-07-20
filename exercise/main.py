from todo.models import Todo
def main():
    print("Todo项目启动成功")
    print("在未来过程中完成增/删/改/查功能")
    first_todo = Todo(1,"背单词",)
    first_todo.complect=True
    Second_todo = Todo(2,"听写",True)
    print(first_todo)
    print(Second_todo)


if __name__ == "__main__":
    main()