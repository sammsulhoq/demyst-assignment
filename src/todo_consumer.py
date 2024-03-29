from src.api_wrapper import APIWrapper

class TodoConsumer:
    def __init__(self):
        self.wrapper = APIWrapper()

    def consume_todos(self):
        for todo_id in range(2, 42, 2):
            todo = self.wrapper.get_todo_by_id(todo_id)
            if todo:
                print(f'Title: {todo["title"]}, Completed: {todo["completed"]}')
            else:
                print(f'Error! Failed to retrieve todo by ID: {todo_id}')
