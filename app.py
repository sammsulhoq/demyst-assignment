from src.todo_consumer import TodoConsumer

def main():
    consumer = TodoConsumer()
    consumer.consume_todos()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f'Error: {e}')
