"""
Orchid AI Web Server
Stage 1.2
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import sys
import os


sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "Core"
    )
)

from orchid import Orchid


orchid = Orchid()


class OrchidServer(BaseHTTPRequestHandler):


    def send_page(self, content):

        self.send_response(200)

        self.send_header(
            "Content-type",
            "text/html"
        )

        self.end_headers()

        self.wfile.write(
            content.encode()
        )


    def do_GET(self):

        url = urlparse(self.path)


        if url.path == "/":

            with open(
                "chat.html",
                "r",
                encoding="utf-8"
            ) as file:

                self.send_page(
                    file.read()
                )


        elif url.path == "/ask":

            data = parse_qs(url.query)

            command = data.get(
                "cmd",
                [""] 
            )[0]


            answer = orchid.command(
                command
            )


            self.send_page(
                answer
            )



server = HTTPServer(
    ("",8000),
    OrchidServer
)


print(
    "🌸 Orchid online at port 8000"
)


server.serve_forever()
