class HTTPResponse:
    def __init__(self, method, url, version):
        self.method = method
        self.url = url
        self.version = version
        self.status_code = 200
        self.status_message = "OK"
        self.headers = {
            "Content-Type": "text/html",
            "Connection": "close"
        }

    def send_response(self, client_socket):
        # Constructing the HTTP response message
        response = f"{self.version} {self.status_code} {self.status_message}\r\n"
        for header, value in self.headers.items():
            response += f"{header}: {value}\r\n"
        response += "\r\n"  # Blank line after headers
        response += "<html><body><h1>Welcome to the Custom HTTP Server</h1></body></html>"

        # Send the response
        client_socket.sendall(response.encode('utf-8'))
        client_socket.close()
