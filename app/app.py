from server import Server


if __name__ == "__main__":
    server = Server(host="0.0.0.0", port=80)
    server.run()
