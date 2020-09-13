from flask import Flask, render_template, request, redirect
import socket
import threading
import requests

from select import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions


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


@app.route('/register', methods=['GET', 'POST'])
# Register
def get_register():
    return render_template('register.html')


# @app.route('/wallet', methods=['GET', 'POST'])
# # Wallet
# def get_wallet():
#     if request.method == 'POST':
#         if __name__ == '__main__':
#             app.run(debug=True)
#     else:
#         return render_template('wallet.html')


@app.route('/transaction', methods=['GET', 'POST'])
# Transaction
def get_transaction():
    if request.method == 'POST':
        admin = request.form['admin']
        searchpass = request.form['pass']
        searchpasscf = request.form['passCf']
        tokenIDadmin = request.form['tokenID']
        valueTransferred = request.form['valueEth']
        address = request.form['idGlobal']
        # print(searchpass)
        # print(searchpasscf)
        # print(tokenIDadmin)
        chromeOptions = ChromeOptions()
        chromeOptions.add_extension('hello.crx')
        driver = webdriver.Chrome(
            'D:\Source code Python\Coin App\chromedriver.exe', options=chromeOptions)
        driver.get(
            "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/create-password/import-with-seed-phrase")

        search = driver.find_element_by_id("password")
        search.send_keys(searchpass)
        search.send_keys(Keys.RETURN)

        search1 = driver.find_element_by_id("confirm-password")
        search1.send_keys(searchpasscf)
        search1.send_keys(Keys.RETURN)

        search0 = driver.find_element_by_class_name("MuiInputBase-input")
        search0.send_keys(tokenIDadmin)
        search0.send_keys(Keys.RETURN)

        botton2 = driver.find_element_by_class_name(
            "first-time-flow__checkbox")
        botton2.click()

        botton = driver.find_element_by_class_name("first-time-flow__terms")
        botton.click()

        bottnxt = driver.find_element_by_class_name("first-time-flow__button")
        bottnxt.click()

        time.sleep(2)

        bttk = driver.find_element_by_class_name("first-time-flow__button")
        bttk.click()

        time.sleep(2)
        bttsend = driver.find_element_by_class_name("btn-secondary")
        bttsend.click()

        time.sleep(2)
        bttidaddress = driver.find_element_by_class_name(
            "ens-input__wrapper__input")
        bttidaddress.send_keys("0x51923d87c096dfEF7962b97A9c315e147302e1e9")

        time.sleep(5)

        ethclick = driver.find_element_by_class_name("unit-input__input")
        ethclick.send_keys(valueTransferred)
        time.sleep(2)

        # nextclick = driver.find_elements_by_xpath(
        #     "//button['data-testid=\"page-container-footer-next\"']")[-1]
        # nextclick.click()
        # time.sleep(2)

        # # confirm button
        # confirmclick = driver.find_elements_by_xpath(
        #     "//button['data-testid=\"page-container-footer-next\"']")[-1]
        # confirmclick.click()

        # time.sleep(5)

        url = "https://api.etherscan.io/api?module=account&action=txlist&address=" + address + \
            "&startblock=0&endblock=99999999&page=1&offset=10&sort=desc&apikey=YourApiKeyToken"

        response = requests.get(url)
        address_content = response.json()
        result = address_content.get("result")

        data = []
        for n, transaction in enumerate(result):
            # tx_from = transaction.get("from"),
            # tx_to = transaction.get("to"),
            # value = transaction.get("value"),
            data.append({
                'tx_from': transaction.get("from"),
                'tx_to': transaction.get("to"),
                'value': transaction.get("value"),
            })

        if data[5]['tx_from'] == admin and data[5]['tx_to'] == address:
            balance = data[5]['value']
            # print(data[5]['value'])
        else:
            balance = "Chua nhap tien"

        return render_template('transaction.html', datas=data, data=balance)
    else:
        return render_template('transaction.html')


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

        return render_template('history.html', datas=data)
    else:
        return render_template('history.html')


if __name__ == '__main__':
    app.run(debug=True)


'''
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
'''
