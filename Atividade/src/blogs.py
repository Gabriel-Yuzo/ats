import requests


class Blog:
    def posts(self):
        endereco = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(endereco)
        return response.json()


    def post_by_user_id(self, userId: int):
        e = f"https://jsonplaceholder.typicode.com/posts/(userId)”"
        response = requests.get(e)
        return response.json()