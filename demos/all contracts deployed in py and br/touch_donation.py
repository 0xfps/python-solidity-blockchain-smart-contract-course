from web3 import Web3
import json
from solcx import compile_standard, install_solc
import os
from dotenv import load_dotenv


load_dotenv()
print("Starting...")

with open("dump/donation_dump.json", "r") as j:
    abi_dump = json.load(j)

# print(abi_dump)
abi = abi_dump['contracts']['donation.sol']['Donation']['abi']

w = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/92d50008e5a84c47adb814475f3a0101"))
# w = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chainId = 4
# chainId = 1337
address = "0x5e078E6b545cF88aBD5BB58d27488eF8BE0D2593"
# address = "0x9dD797f7aD7D1c431fC1d9140F86ed5BE7b545ED"
private_key = os.getenv("PRIVATE_KEY")
nonce = w.eth.getTransactionCount(address)

# contract_address = "0x27cDFf52aF89696ea8Dd92D8cb511f5DF2B720C9"
contract_address = "0x97B97e01702cfD140C8c2aaa5a88d263E236d0ae"

donation_interact = w.eth.contract(address=contract_address, abi=abi)
print(donation_interact)



print("""
Welcome to our Crowdfunding.
You can donate any amount of dollar above $3;
enter 'exit' to leave the funding.
""")

print("Deploying...")
print(donation_interact.functions.See_Length().call())
new_donation_build = donation_interact.functions.Donate(50).buildTransaction(
{ 
    "gasPrice": w.eth.gas_price, 
    "chainId": chainId, 
    "from": address, 
    "nonce": nonce
})


new_donation_sign = w.eth.account.sign_transaction(new_donation_build, private_key=private_key)
new_donation_send = w.eth.send_raw_transaction(new_donation_sign.rawTransaction)
new_donation_receipt = w.eth.wait_for_transaction_receipt(new_donation_send)
print(donation_interact.functions.See_Length().call())
print("Deployed!!")


# money = input("Enter new funding amount >> ")

# if money.lower() == "exit":
#     print("You have left this crowdfunding. Thank you.")

# else:
#     try:
#         funds = int(money)
        
#         if funds < 4:
#             print("We only take funds above 3 dollars.")
        
#         else:
#             print("Deploying...")
            # print(donation_interact.functions.See_Length().call())
#             new_donation_build = donation_interact.functions.Donate(50).buildTransaction({
#                 "gasPrice": w.eth.gas_price, 
#                 "chainId": chainId, 
#                 "from": address, 
#                 "nonce": nonce + 5
#             })
#             new_donation_sign = w.eth.account.sign_transaction(new_donation_build, private_key=private_key)
#             new_donation_send = w.eth.send_raw_transaction(new_donation_sign.rawTransaction)
#             new_donation_receipt = w.eth.wait_for_transaction_receipt(new_donation_send)
#             print("Deployed!!")
        
    
#     except:
#         print("We dont take that.")