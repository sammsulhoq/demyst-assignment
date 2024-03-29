import requests

class APIWrapper:
    def get_todo_by_id(self, todo_id):
        try:
            url = f'https://jsonplaceholder.typicode.com/todos/{todo_id}'
            response = requests.get(url)
            response.raise_for_status()  # Raise exception for non-2xx responses
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f'HTTP Error: {e}')
            return None
        except requests.exceptions.RequestException as e:
            print(f'Error: {e}')
            return None
