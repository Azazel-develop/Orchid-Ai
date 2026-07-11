"""
Orchid AI - Web Interface
Stage 1
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import sys
import os


# Connect to Core folder
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


    def do_GET(self):

        if self.path == "/":

            page = """
            <!DOCTYPE html>
            <html>
            <head>
            <title>Orchid AI</title>

            <style>
            body {
                font-family: Arial;
                text-align:center;
                margin-top:50px;
            }

            input {
                width:300px;
                padding:10px;
            }

            button {
                padding:10px;
            }

            #answer {
                margin-top:20px;
            }

            </style>

            </head>

            <body>

            <h1>🌸 Orchid AI</h1>

            <input id="cmd"
            placeholder="Talk to Orchid">

            <button onclick="send()">
            Send
            </button>

            <div id="answer"></div>


            <script>

            function send(){

                let command =
                document.getElementById("cmd").value;


                fetch(
                "/ask?cmd="
                + encodeURIComponent(command)
                )

                .then(
                response => response.text()
                )

                .then(
                data =>
                document.getElementById("answer")
                .innerHTML=data
                );

            }

            </script>


            </body>
            </html>
            """

            self.send_response(200)
            self.send_header(
                "Content-type",
                "text/html"
            )
            self.end_headers()

            self.wfile.write(
                page.encode()
            )


    def do_ASK(self):
        pass



    def do_GET_ASK(self, command):

        response = orchid.command(command)

        return response



server = HTTPServer(
    ("",8000),
    OrchidServer
)

print(
    "Orchid running on port 8000"
)

server.serve_forever()
