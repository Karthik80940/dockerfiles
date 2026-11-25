import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

name = os.getenv("MY_NAME", "Guest")
city = os.getenv("MY_CITY", "Unknown")
port = int(os.getenv("PORT", "8000"))

print(f"Hello {name} from {city}",flush=True)
print(f"Server running on port {port}",flush=True)

HTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler).serve_forever()