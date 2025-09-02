import requests
import json

BASE = "http://127.0.0.1:8000"


class Client:
    def __init__(self, base_url=BASE):
        self.base_url = base_url

    def get_home(self):
        response = requests.get(f"{self.base_url}/")
        print("Codigo:", response.status_code)
        if response.status_code == 200:
            print("Contenido recibido (HTML):")
            print(response.text[:200], "...")
        else:
            print("Error:", response.text)

    def get_products(self):
        response = requests.get(f"{self.base_url}/api/products")
        print("Codigo:", response.status_code)
        if response.status_code == 200:
            print("Productos:")
            print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        else:
            print("Error:", response.text)
