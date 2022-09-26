from datetime import datetime as dt

tasks = [
	{
        "id": 1,
        "name": "勉強",
        "done": False
    },
    {
    	"id": 2,
        "name": "買い物",
        "done": False
    },
    {
    	"id": 3,
        "name": "昼寝",
        "done": False
    }
]

todo_input = Element("todo_input")
todo_template = Element("todo_template").select(".todo", from_content=True)
todo_list = Element("todo_list")

def init():
    for task in tasks:
        createList(task)

def createList(task):
        todo_html = todo_template.clone(task["id"], to=todo_list)
        todo_html_content = todo_html.select("label")
        todo_html_input = todo_html_content.select("input")
        todo_html_text = todo_html_content.select("#todo_text")
        todo_html_input.element.value = task["name"]
        todo_html_text.element.innerText = task["name"]
        todo_list.element.appendChild(todo_html.element)

def addTodo(*ags, **kws):
    newTask = {
        "id": dt.now(),
        "name": todo_input.element.value,
        "done": False
    }
    tasks.append(newTask)
    createList(newTask)
    todo_input.element.value = ""

if __name__ == "__main__":
    init()