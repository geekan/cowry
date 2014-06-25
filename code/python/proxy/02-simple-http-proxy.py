import SocketServer
import SimpleHTTPServer
import urllib

PORT = 8000

class Proxy(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.copyfile(urllib.urlopen(self.path), self.wfile)

httpd = SocketServer.ForkingTCPServer(('', PORT), Proxy)
print "serving at port", PORT
httpd.serve_forever()
