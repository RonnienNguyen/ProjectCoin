from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))

# print(web3.isConnected())
# print(web3.eth.blockNumber)
account1 = "0x6C6ff672aF82146E1eC92D9CE3565F082e97D51B"
account2 = "0x86728dBF39B1BB357a9f1AeBFf5Bb871BF5C8557"

private_key = "b081be9fdc31299b9af2f6baf504a36fc74c110fc9248396fe772479d88909d2"

# Get the nonce

nonce = web3.eth.getTransactionCount(account1)

# Xay 1 giao dich
tx = {
    'nonce': nonce,
    'to': account2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}
# Sign Transaction

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))

# Send Transaction


# Get Transaction Hash
