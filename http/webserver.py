from http.server import HTTPServer, BaseHTTPRequestHandler


class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Hello, World!'.encode())


def main():
    PORT=8080
    server = HTTPServer(server_address=('localhost', PORT), RequestHandlerClass=WebServerHandler)
    print("Server running on port {}".format(PORT))
    server.serve_forever()


if __name__ == "__main__":
    main()
