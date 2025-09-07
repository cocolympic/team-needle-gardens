import socketserver

class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.sendall(b"Hello!\n")

with socketserver.TCPServer(("localhost", 5000), Handler) as server:
    server.serve_forever()