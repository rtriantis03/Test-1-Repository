import socket
import threading
from request_handler import RequestHandler
from logger import Logger

class HTTPServer:
    def __init__(self, host='127.0.0.1', port=8080):
        self.host = host
        self.port = port
        self.logger = Logger()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

    def start(self):
        self.logger.log(f"Server started at {self.host}:{self.port}")
        while True:
            client_socket, client_address = self.server_socket.accept()
            self.logger.log(f"Connection established with {client_address}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        handler = RequestHandler(client_socket, self.logger)
        handler.handle_request()

if __name__ == "__main__":
    server = HTTPServer()
    server.start()
