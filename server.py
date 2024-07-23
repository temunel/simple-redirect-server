import http.server
import socketserver
import base64

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # get the request url
        print("Request URL:", self.headers['Host'] + self.path)

        # get the base url
        base_url = self.path[1:]
        print("Base URL:", base_url)

        # get the redirection url
        try:
            # decode the base url
            redirection_url = base64.b64decode(base_url).decode('utf-8')
        except Exception as e:
            self.send_error(400, str(e))
            return

        if not redirection_url:
            self.send_error(400, "Invalid URL format: Decoded URL is empty")
            return

        print("Decoded Redirection URL:", redirection_url)
        
        # redirect to decoded redirection url
        self.send_response(302)
        self.send_header('Location', redirection_url)
        self.end_headers()

        print("Request processed successfully")


HOST = 'localhost'
PORT = 8080

handler = MyRequestHandler
httpd = socketserver.TCPServer((HOST, PORT), handler)
print('Server started')
httpd.serve_forever()