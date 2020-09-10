import requests




address = "0x51923d87c096dfEF7962b97A9c315e147302e1e9"
admin = "0x51923d87c096dfEF7962b97A9c315e147302e1e9"


url = "https://api.etherscan.io/api?module=account&action=txlist&address=" + address + "&startblock=0&endblock=99999999&page=1&offset=10&sort=desc&apikey=YourApiKeyToken"

response = requests.get(url)
#
# print(response.json())


address_content = response.json()

result = address_content.get("result")

for n, transaction in enumerate(result):
    hash = transaction.get("hash")
    tx_from = transaction.get("from")
    tx_to = transaction.get("to")
    value = transaction.get("value")
    confirmations = transaction.get("confirmation")

    print("Transaction ID: ", n)
    print("hash: ", hash)
    print("from: ", tx_from)
    print("To: ", tx_to)

    if tx_from == address:
        print("Sending")

    print("Value: ", value)
    print("Confirmations: ", confirmations)
    print("\n")











