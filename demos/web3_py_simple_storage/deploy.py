from solcx import compile_standard, install_solc
import json
from  web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()
"""
    We are going to read the contents of our solidity file,
    In that way, we can know what its gonna deploy
"""

with open("SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()


#compiling solidity

install_solc("0.6.0")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": 
        {
            "SimpleStorage.sol":
            {
                "content": simple_storage_file
            }
        },
        "settings":
        {
            "outputSelection":
            {
                "*":
                {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                }
            }
        },
    },
    solc_version="0.6.0",
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

#get the bytecode.
# We have to carefully read the dumped json in the compiled_code.json file to get the proper path to the bytecode.
bytecode = compiled_sol['contracts']['SimpleStorage.sol']['SimpleStorage']['evm']['bytecode']['object']

# get abi
# from the read file, abi should return a list of dictionaries
abi = compiled_sol['contracts']['SimpleStorage.sol']['SimpleStorage']['abi']



# conncecting to the ganche
# w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/92d50008e5a84c47adb814475f3a0101"))

#for the blockchain chain id
# chain_id = 5777
# chain_id = 1337
chain_id = 4

#address to deploy from
# address = "0x38835A37ff090269986bE16Aae819EFf233f8108"
# address = "0x203b8CbDd2Ee38216f9d1B7F469574Ef223e9032"
# metamask address
address = "0x5e078E6b545cF88aBD5BB58d27488eF8BE0D2593"

#private key for transaction signing

private_key = os.getenv("PRIVATE_KEY")
# docs https://web3py.readthedocs.io
# docs https://
# print(private_key)

 

#create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

#get the nonce
nonce = w3.eth.getTransactionCount(address)
# print(nonce)

# Build a transaction
# Sign a transaction
# Send a transaction

print("Deploying...")
# Building the transaction
transaction = SimpleStorage.constructor().buildTransaction({
    "gasPrice": w3.eth.gas_price, 
    "chainId": chain_id, 
    "from": address, 
    "nonce": nonce
})

# Signing
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
# print(signed_txn)

# Sending

tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Deployed!")


simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# Initial value of original number
print(simple_storage.functions.retrieve().call())

store_transaction = simple_storage.functions.store(15).buildTransaction({
    "gasPrice": w3.eth.gas_price, 
    "chainId": chain_id, 
    "from": address, 
    "nonce": nonce + 1
})

signed_store_tx = w3.eth.account.sign_transaction(store_transaction, private_key=private_key)
print("Updating...")
send_store_tx = w3.eth.send_raw_transaction(signed_store_tx.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_tx)
print("Updated!")
print(simple_storage.functions.retrieve().call())