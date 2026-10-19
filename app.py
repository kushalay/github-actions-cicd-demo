from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class ApplicationHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            response = {
                "application": "GitHub Actions CI/CD Demo",
                "status": "running"
            }
            self.send_response(200)

        elif self.path == "/health":
            response = {
                "status": "healthy"
            }
            self.send_response(200)

        else:
            response = {
                "error": "Not Found"
            }
            self.send_response(404)

        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

    def log_message(self, format, *args):
        print(format % args)


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), ApplicationHandler)
    print("Application listening on port 8000")
    server.serve_forever()
