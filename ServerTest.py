from flask import Flask, render_template, request, redirect
import socket
import threading
import requests

app = Flask(__name__)

USERNAME = 'admin'
PASSWORD = 'admin'


@app.route('/signin', methods=['GET', 'POST'])
# Signin
def get_signin():
    if request.method == 'POST':
        username = request.form['fname']
        password = request.form['fpass']
    else:
        return render_template('signin.html')
    if username == USERNAME and password == PASSWORD:
        return redirect('/history')
    else:
        return redirect('/signin')


@app.route('/history', methods=['GET', 'POST'])
# History
def get_response():
    if request.method == 'POST':
        idGlobal = request.form['idglobal']

        # address = "0x51923d87c096dfEF7962b97A9c315e147302e1e9"
        address = idGlobal
        admin = "0x51923d87c096dfEF7962b97A9c315e147302e1e9"
        url = "https://api.etherscan.io/api?module=account&action=txlist&address=" + address + \
            "&startblock=0&endblock=99999999&page=1&offset=10&sort=desc&apikey=YourApiKeyToken"

        response = requests.get(url)
        address_content = response.json()
        result = address_content.get("result")

        data = []
        for n, transaction in enumerate(result):
            data.append({'hash': transaction.get("hash"),
                        'timeStamp': transaction.get("time"),
                        'tx_from': transaction.get("from"),
                        'tx_to': transaction.get("to"),
                        'value': transaction.get("value"),
                        'fee': transaction.get("gasPrice"),
                        'confirmation': transaction.get("confirmation")})
        print(data)
        return render_template('history.html', datas=data)
    else:
        return render_template('history.html')

        


# @app.route('/transaction', methods=['GET', 'POST'])
# def


SERVER = socket.gethostbyname(socket.gethostname())


httpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# re-use the port if server crack
httpserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# httpserver.bind(ADDR)


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


if __name__ == '__main__':
    app.run(debug=True)
