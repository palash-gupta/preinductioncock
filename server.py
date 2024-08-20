import http.server
import socketserver
import cgi
import cv2 as cv
import pickle

PORT = 90

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Parse the form data posted
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type']}
        )

        # Extract file information
        if 'file' in form:
            file_item = form['file']
            if file_item.filename:
                # Save the file in the current directory
                with open(file_item.filename, 'wb') as output_file:
                    output_file.write(file_item.file.read())
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"File uploaded successfully!")
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"No file was uploaded")
        elif 'data' in form:
            data_item = form['data']

            frame = pickle.loads(data_item)
            cv.imshow("webcam feed", frame)


        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"No file was uploaded")



with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()

