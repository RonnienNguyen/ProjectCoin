import json
from web3 import Web3


ganache_url = "http://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]')
address = web3.toChecksumAddress("0x7dB6c4CAb7a233F36bBACA698bA6C6E269e539f9")

contract = web3.eth.contract(address=address, abi=abi)

print(contract.functions.greet().call())


tx_Hash = contract.functions.setGreeting('THIENPHUC').transact()


print(tx_Hash)

web3.eth.waitForTransactionReceipt(tx_Hash)

print('Updated greeting: {}'.format(
    contract.functions.greet().call()
))
