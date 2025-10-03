#0310 2025
#12:58
#python api klass
#make a server

from http.server import BaseHTTPRequestHandler, HTTPServer
import time

host_name = "localhost"
server_port = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><head><title>Hello!</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example of a webserver.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
    
    def do_GET

if __name__ == "__main__":
    webServer = HTTPServer((host_name, server_port), MyServer)
    print("server started at http://%s:%s" % (host_name, server_port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server.close()
    print("servre stopped")