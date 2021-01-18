from http.server import HTTPServer, BaseHTTPRequestHandler

task_list = ['T1', 'T2', 'T3']

class TaskServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        output = ''
        output += '<html><body>'
        output += '<h1>Task List </h1>'
        for task in task_list:
            output += task
            output += '</br>'
        output += '</html></body>'
        self.wfile.write(output.encode())


def main():
    PORT=8080
    server = HTTPServer(server_address=('localhost', PORT), RequestHandlerClass=TaskServerHandler)
    print("Server running on port {}".format(PORT))
    server.serve_forever()


if __name__ == "__main__":
    main()
