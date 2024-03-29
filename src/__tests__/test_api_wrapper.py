from src.api_wrapper import APIWrapper

def test_get_todo_by_id():
    wrapper = APIWrapper()
    
    todo = wrapper.get_todo_by_id(1)
    assert todo is not None 
    assert todo['id'] == 1

    todo_invalid = wrapper.get_todo_by_id(1000)
    assert todo_invalid is None 
