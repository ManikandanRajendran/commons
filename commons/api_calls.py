import requests

def fetch_all_books(self):
        response = requests.get(url="http://127.0.0.1:5000/v1/resources/books/all")
        return response