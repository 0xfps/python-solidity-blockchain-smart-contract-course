from web3 import Web3
import json
from solcx import compile_standard, install_solc
import os
from dotenv import load_dotenv

load_dotenv()
print("Starting...")

with open("donation.sol", "r") as file:
    donation_file = file.read()

print("Compiling contract...")
install_solc("0.8.12")

compiled_file = compile_standard(
    {
        "language": "Solidity",
        "sources": 
        {
            "donation.sol":
            {
                "content": donation_file
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
    solc_version="0.8.12"
)

with open("dump/donation_dump.json", "w") as dumpfile:
    json.dump(compiled_file, dumpfile)

print("Compiled!!!")

bytecode = compiled_file['contracts']['donation.sol']['Donation']['evm']['bytecode']['object']
abi = compiled_file['contracts']['donation.sol']['Donation']['abi']


w = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/92d50008e5a84c47adb814475f3a0101"))
# w = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chainId = 4
# chainId = 1337
address = "0x5e078E6b545cF88aBD5BB58d27488eF8BE0D2593"
# address = "0x9dD797f7aD7D1c431fC1d9140F86ed5BE7b545ED"
private_key = os.getenv("PRIVATE_KEY")
nonce = w.eth.getTransactionCount(address)

print("Deploying contract...")
donation_contract = w.eth.contract(abi=abi, bytecode=bytecode)
donation_build = donation_contract.constructor().buildTransaction({
    "gasPrice": w.eth.gas_price, 
    "chainId": chainId, 
    "from": address, 
    "nonce": nonce
})

donation_sign = w.eth.account.sign_transaction(donation_build, private_key=private_key)
donation_send = w.eth.send_raw_transaction(donation_sign.rawTransaction)
donation_receipt = w.eth.wait_for_transaction_receipt(donation_send)

donation_contract_address = donation_receipt.contractAddress
print("Deployed!!!")

print("Logging address and abi...")
with open("contracts/donation_contract.txt", "w") as cont:
    cont.write("Contract: Donation.sol\n")
    cont.write("Contract Address: "+ donation_contract_address +"\n")
    cont.write("ABI: "+ str(abi) +"\n")
print("Logged!!!")
print("Finished!!!")