from todo import Todo
from todolist import TodoList
from datetime import datetime


task = Todo("uno",datetime.now(),datetime.now(),"Torino")
task2 = Todo("due",datetime.now(),datetime.now(),"Torino")
todolist = TodoList("mia lista")
todolist.add_todo(task)
todolist.add_todo(task2)
print(todolist)

'''
print(task.is_completato)

for evento in todolist.list:
    if evento.nome == "uno":
        evento.completa()
    
print(task.is_completato)
'''
todolist.trova_e_completa("due")
print(todolist)
