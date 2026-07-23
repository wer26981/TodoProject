from todo.services import TodoServices
def main():
    '''svc = TodoServices()
    a = svc.add("Buy milk")
    b = svc.add("Walk the dog")
    print("增加功能:",svc.list_all())
    
    svc.update(a.id,completed=True)
    svc.update(b.id,completed=True)
    print("更新功能:",svc.list_all())
    
    svc.delete(a.id)
    print("删除功能:",svc.list_all())'''
    svc = TodoServices()
    svc.add("Buy milk","Buy milk from the store")
    
if __name__ == "__main__":
    main()