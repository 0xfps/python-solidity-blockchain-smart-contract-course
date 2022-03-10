"""
    These 4 things are constants to be imported for now in the lesson that goes on
"""
from solcx import compile_standard, install_solc
import os
from dotenv import load_dotenv
import json
from  web3 import Web3

load_dotenv()


"""
    Reading the contents of the solidity file i want to work with first
"""

with open("calc.sol", "r") as my_sol_file:
    calcfile = my_sol_file.read()

"""
    Reading done
        |
        |
        |
        |
        |
        |
        |
        \/

    Compilation
"""

install_solc("0.8.12")

compiled_file = compile_standard(
    {
        "language": "Solidity",
        "sources": 
        {
            "calc.sol":
            {
                "content": calcfile
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


"""
    dump the compiled calc.sol file into a json file
"""

with open("dumpcalc.json", "w") as dumpfile:
    json.dump(compiled_file, dumpfile)

"""
    File dumped success, we move
"""

"""
    Deploying the  file

    Before deploying i have to get the bytecode and the abi
"""

mybytecode = compiled_file['contracts']['calc.sol']['math']['evm']['bytecode']['object']

myabi = compiled_file['contracts']['calc.sol']['math']['abi']


"""
    INitiate web3 and Set necessary variables for deployment
"""

w = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chainId = 1337
myaddress = "0x203b8CbDd2Ee38216f9d1B7F469574Ef223e9032"
pkey = os.getenv("PRIVATE_KEY")
nonce = w.eth.getTransactionCount(myaddress)

"""
    Create a contract for deployment
"""

deploy_calc = w.eth.contract(abi=myabi, bytecode=mybytecode)

"""
    BSS
    B -> Build
    S -> Sign
    S -> Send
"""

# build
build_calc = deploy_calc.constructor().buildTransaction({
    "gasPrice": w.eth.gas_price, 
    "chainId": chainId, 
    "from": myaddress, 
    "nonce": nonce
})

# sign
sign_calc = w.eth.account.sign_transaction(build_calc, private_key=pkey)

# send
send_calc = w.eth.send_raw_transaction(sign_calc.rawTransaction)
# returns hash

# receipt
receipt_calc = w.eth.wait_for_transaction_receipt(send_calc)
# returns receipt containing transaction address


"""
    Time to communicate with my contract

    create a contract for communication
"""
com_calc = w.eth.contract(address=receipt_calc.contractAddress, abi=myabi)

#new builds etc
newbuild = com_calc.functions.sub(12, 5).buildTransaction({
    "gasPrice": w.eth.gas_price, 
    "chainId": chainId, 
    "from": myaddress, 
    "nonce": nonce + 1
})

# sign
sign_calc2 = w.eth.account.sign_transaction(newbuild, private_key=pkey)

# send
send_calc2 = w.eth.send_raw_transaction(sign_calc2.rawTransaction)
# returns hash

# receipt
receipt_calc2 = w.eth.wait_for_transaction_receipt(send_calc2)
# returns receipt containing transaction address

print(com_calc.functions.sub(12, 5).call())