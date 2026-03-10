from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Test</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #fff;
        }
        .container {
            text-align: center;
            padding: 2rem;
        }
        h1 { font-size: 3rem; margin-bottom: 1rem; }
        p { font-size: 1.2rem; opacity: 0.9; margin-bottom: 2rem; }
        .card {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            border-radius: 12px;
            padding: 2rem;
            max-width: 500px;
            margin: 0 auto;
        }
        .card h2 { font-size: 1.5rem; margin-bottom: 0.5rem; }
        .card p { font-size: 1rem; opacity: 0.8; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello from Python</h1>
        <p>A simple single-page site served with Python</p>
        <div class="card">
            <h2>It works!</h2>
            <p>This page is served by a lightweight Python HTTP server.</p>
        </div>
    </div>
</body>
</html>"""


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(HTML.encode())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"Server running at http://localhost:{port}")
    server.serve_forever()
