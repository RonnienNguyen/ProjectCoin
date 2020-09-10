from flask import Flask, render_template, request, redirect
import socket
import threading

app = Flask(__name__)

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 1501
ADDR = (SERVER, PORT)
USERNAME = 'admin'
PASSWORD = 'admin'


httpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# re-use the port if server crack
httpserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
httpserver.bind(ADDR)


def GET_request(filename):
    if(filename == 'signin.html'):
        return False
    return True


def POST_request(filename, request_body): 
    username = request_body.split('&')[0].split('=')[1]
    password = request_body.split('&')[1].split('=')[1]
    # email = request_body.split('&')[2].split('=')[1]
    # confirm = request_body.split('&')[3].split('=')[1]
    if(username == USERNAME and password == PASSWORD):
        return True
    return False


def send_response(client, filename, status):
    with open(filename, 'rb') as f:
        body = f.read()
    header = 'HTTP/1.1' + status + '\n'
    if(filename.endswith(".jpg")):
        mimetype = 'image/jpg'
    elif(filename.endswith(".css")):
        mimetype = 'text/css'
    else:
        mimetype = 'text/html'
    header += 'Content-Type: '+str(mimetype)+'\n\n'
    response_msg = header.encode('utf8') + body
    client.send(response_msg)


# @app.route('/history.html', methods=['GET', 'POST'])
# def get_response():
#     if request.method == 'POST':
#         idPlatform = request.form['idplatform']
#         return redirect('/history.html')
#     else:
#         return render_template('history.html')

    



def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    request = conn.recv(1024).decode('utf8')
    request_detail = request.split(' ')
    method = request_detail[0]
    requesting_file = request_detail[1][1:]
    if(requesting_file == ''):
        requesting_file = 'history.html'
    flag = True
    if(method == 'GET'):
        flag = GET_request(requesting_file)
    else:
        flag = POST_request(requesting_file, request.split('\n')[-1])
    if(flag == True):
        send_response(conn, requesting_file, '200 OK')
    else:
        send_response(conn, 'transaction.html', 'Transaction')
    conn.close()
    print(f"[DISCONNECT] {addr} has disconnected")


def start():
    httpserver.listen(10)
    print(f"[LISTENING] Server is listening on {ADDR}...")
    try:
        while True:
            conn, addr = httpserver.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
    except Exception:
        httpserver.close()
    finally:
        httpserver.close()


print("[STARTING] Waiting for client...")
start()
