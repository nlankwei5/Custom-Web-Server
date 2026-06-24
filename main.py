import socket 
import time

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(5)


print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}...")

while True:
        client_socket, client_address = server_socket.accept()
        request = client_socket.recv(1500).decode('utf-8')
        print(f"[*] Received request from {client_address}: {request}")
        headers = request.split('\n')
        first_header_component = headers[0].split()
        
        http_method = first_header_component[0]
        http_path = first_header_component[1]
        
        if http_method == 'GET':
            if http_path == '/':
                with open('index.html', 'r') as f:
                    response_body = f.read()
                    f.close()
                response = 'HTTP/1.1 200 OK\n\n' + response_body
            else:
                response = 'HTTP/1.1 404 NOT FOUND\n\n<h1>404 Not Found</h1>'
        else:
            response = 'HTTP/1.1 405 METHOD NOT ALLOWED\n\nALLOWED METHODS: GET'
            

        client_socket.sendall(response.encode('utf-8'))
        client_socket.close()

    


