from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        message = (
            "<h1>🛡️ Eng. Zeinab's Cloud Fortress is Running Securely!</h1>"
        )
        self.wfile.write(bytes(message, "utf8"))

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), SimpleServer)
    print("Server running on port 8080...")
    server.serve_forever()
