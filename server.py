import os
import http.server
import socketserver

from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        # HTML content to serve
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <title>Coming Soon Page</title>
        <style>
            .verdana-bold {
                font-family: 'Verdana', sans-serif;
                font-weight: bold;
            }
        </style>
        </head>
        <body>
            <p class="verdana-bold">Coming Soon!</p>
            <p>Discover, Engage, and Grow with Us!</p>
            <p>We're busy crafting a unique space where inspiration meets practical advice.</p>
            <p>Our blog and YouTube channel will soon be your go-to resources for insightful, thought-provoking content that sparks your curiosity and fuels your personal and professional growth.</p>
        </body>
        </html>
        """
        
        # Write the HTML content to wfile
        self.wfile.write(html_content.encode('utf-8'))

port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
