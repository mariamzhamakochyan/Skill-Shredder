from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Skill-Shredder')

def run_server():
    host = 'localhost'
    port = 8000

    server_address = (host, port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f'Server running at http://{host}:{port}')

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down the server...')
        httpd.server_close()

if __name__ == '__main__':
    run_server()

