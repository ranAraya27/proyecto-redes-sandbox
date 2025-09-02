from client import Client


if __name__ == "__main__":
    client = Client()
    print("== Pagina principal ==")
    client.get_home()
    print("\n== Lista de productos ==")
    client.get_products()
