import requests

class SimpleAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_posts(self):
        url = f"{self.base_url}/posts"
        return requests.get(url).json()

    def create_post(self, title, body, user_id):
        url = f"{self.base_url}/posts"
        data = {"title": title, "body": body, "userId": user_id}
        return requests.post(url, json=data).json()

#fectching posts
client = SimpleAPIClient("https://jsonplaceholder.typicode.com")
posts = client.get_posts()
print("First Post Title:", posts[0]["title"])

#creating a new post
client = SimpleAPIClient("https://jsonplaceholder.typicode.com")
new_post = client.create_post("My Title", "My Body", 1)
print("Created Post:", new_post)