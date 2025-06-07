class RedisServer:
    def __init__(self, host='localhost', port=6379):
        self.host = host
        self.port = port
        self.database = Database()
        self.protocol_handler = ProtocolHandler()

    def start(self):
        import socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")

        while True:
            client_socket, addr = server_socket.accept()
            print(f"Connection from {addr}")
            self.handle_client(client_socket)

    def handle_client(self, client_socket):
        with client_socket:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                response = self.process_request(data)
                self.protocol_handler.write_response(client_socket, response)

    def process_request(self, data):
        command = data.decode('utf-8').strip()
        return self.database.execute_command(command)