def server():
    print("Receiving...")
    return {"data": "Hello, world!"}


if __name__ == '__main__':
    client = server()
    print(client)
