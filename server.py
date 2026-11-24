from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Only allow homepage
        if self.path == "/" or self.path == "/index.html":
            with open("index.html", "rb") as f:
                data = f.read()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(data)
        else:
            # Hide all other files
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 - Page Not Found")

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()