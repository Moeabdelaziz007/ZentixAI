import json
from http.server import SimpleHTTPRequestHandler, HTTPServer

from zero_system import ZeroSystem


system = ZeroSystem()


class DashboardHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/status.json":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            status = system.system_status()
            self.wfile.write(json.dumps(status, ensure_ascii=False).encode("utf-8"))
        else:
            super().do_GET()


def run(server_class=HTTPServer, handler_class=DashboardHandler):
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    print("Serving on http://localhost:8000/")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
