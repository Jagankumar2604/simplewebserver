from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>Jagan+</title>
    </head>
    <body>
        <h1 align="center">Device specification-25012671</h1>
        <br>
        <center>
            <table border="3" cellspacing="5" callpading="5">

        </center>
            <tr>
                <th>S.no</th>
                <th>Device specification</th>
                <th>Description</th>
            </tr>

            <tr>
                <td>1</td>
                <td>storage</td>
                <td>1Tb</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Grahpics card</td>
                <td>128MB</td>
            </tr>
            <tr>
                <td>3</td>
                <td>installed ram</td>
                <td>16.0GB</td>
            </tr>
            <tr>
                <td>4</td>
                <td>processor</td>
                <td>Intel core ultra5</td>
            </tr>
            <tr>
                <td>5</td>
                <td>Device Name</td>
                <td>Acer</td>
            </tr>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()