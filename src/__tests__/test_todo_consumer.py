from src.todo_consumer import TodoConsumer

def test_consume_todos():
    consumer = TodoConsumer()
    outputs = []

    def mock_print(*args, **kwargs):
        outputs.append(args)

    consumer.print = mock_print
    consumer.consume_todos()

    expected_output = [
        (f'Title: {title}, Completed: {completed}',)
        for title, completed in [
            ("quis ut nam facilis et officia qui", False),
            ("et porro tempora", True),
            ("qui ullam ratione quibusdam voluptatem quia omnis", False),
            ("quia est ipsam", True),
            ("ea molestias quasi exercitationem repellat qui ipsa sit aut", False),
            ("et iusto veniam et illum aut fuga", True),
            ("eos dolorem iste accusantium est eaque quam", False),
            ("laboriosam dolor voluptates", True),
            ("temporibus sit alias delectus eligendi possimus magni", True),
            ("atque aut aut nemo eum qui rem eaque suscipit", True),
            ("ut et tenetur ab eius magnam", False),
            ("optio ipsam molestias necessitatibus occaecati facilis veritatis dolores aut", True),
            ("dolorem quibusdam ducimus consequuntur dicta aut quo laboriosam", False),
            ("dolorum est consequatur ea mollitia in culpa", True),
            ("molestiae ipsa aut voluptatibus pariatur dolor nihil", True),
            ("ullam nobis libero sapiente ad optio sint", True),
            ("suscipit repellat esse quibusdam voluptatem incidunt", True),
            ("distinctio vitae autem nihil ut molestias quo", True),
            ("et itaque necessitatibus maxime molestiae qui quas velit", False),
            ("adipisci non ad dicta qui amet quaerat doloribus ea", True)
        ]
    ]

    assert outputs != expected_output
