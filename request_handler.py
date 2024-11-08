from url_parser import URLParser
from response import HTTPResponse

class RequestHandler:
    def __init__(self, client_socket, logger):
        self.client_socket = client_socket
        self.logger = logger

    def handle_request(self):
        request_data = self.client_socket.recv(1024).decode('utf-8')
        if not request_data:
            self.client_socket.close()
            return

        self.logger.log(f"Request received: {request_data}")

        # Parse the request
        method, url, version = self.parse_request(request_data)

        # Create a response
        response = HTTPResponse(method, url, version)
        response.send_response(self.client_socket)

    def parse_request(self, request_data):
        lines = request_data.splitlines()
        method, url, version = lines[0].split()
        self.logger.log(f"Method: {method}, URL: {url}, Version: {version}")
        return method, url, version
