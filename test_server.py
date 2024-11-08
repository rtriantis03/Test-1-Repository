import unittest
from server import HTTPServer
from unittest.mock import patch, MagicMock

class TestHTTPServer(unittest.TestCase):
    @patch('server.socket.socket')
    def test_server_start(self, mock_socket):
        mock_socket.return_value.accept.return_value = (MagicMock(), ('127.0.0.1', 8080))
        server = HTTPServer()
        server.start()

    @patch('server.RequestHandler')
    def test_handle_client(self, mock_request_handler):
        server = HTTPServer()
        mock_request_handler.handle_request = MagicMock()
        server.handle_client('mock_socket')
        mock_request_handler.handle_request.assert_called_once()

if __name__ == "__main__":
    unittest.main()
