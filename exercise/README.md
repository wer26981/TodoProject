主要目标完成命令行Todo(待处理事件)管理器(命令行版的备忘录)
day02:
完成命令行Todo管理器的基本框架
data文件夹存放Todo事件的数据,todos.json将数据以.json的格式保存
todo文件夹属于flat layout项目结构,便于项目完成后打包上传
__init.py作为可导入包的标记
models.py用于后续定义Todo事件的数据结构,比如一个Todo事件该有哪些字段,id,名称,完成情况等
services.py用于后续完成增/删/改/查功能模块
storage.py用于后续完成数据库的读写操作,也就是将Todo事件传入todos.json,以及读取todos.json里的Todo事件
todos.json做为数据库存储数据
day03需要完成Todo事件的数据结构

day03:完成Todo事件的数据结构
Todo事件的数据结构为:id(编号),name(待完成事件),complect(是否完成?)=False
初始化对象使用的是@dataclass,在使用@dataclass时我们需要先导入form dataclasses import dataclass
然后创建Todo事件的数据结构
在main中进行测试时,需要先对编写的models.py进行保存,然后from todo.models import Todo
因为我们需要创建不同的todo对象,所以我们需要导入Todo类来进行实例化(也就是通过类的模板来创建对应的实例),又因为main.py与models.py不在同一级文件夹下,所以导入时需要通过todo.models导入
最后我在main()方法中创建了两个todo测试用例,能够成功运行,要注意传入参数时格式不能出错

