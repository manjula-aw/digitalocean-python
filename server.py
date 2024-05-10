import os
import http.server
import socketserver

from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        msg = "Coming Soon!"
        self.wfile.write(msg.encode())
        msg = "Discover, Engage, and Grow with Us!"
        self.wfile.write(msg.encode())
        msg = "We're busy crafting a unique space where inspiration meets practical advice. "
        self.wfile.write(msg.encode())
        msg = "Our blog and YouTube channel will soon be your go-to resources for insightful, thought-provoking content that sparks your curiosity and fuels your personal and professional growth."
        self.wfile.write(msg.encode())


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
