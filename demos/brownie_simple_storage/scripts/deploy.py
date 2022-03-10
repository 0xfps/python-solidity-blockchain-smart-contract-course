# to get an array of simple accounts addresses
from brownie import accounts, config, SimpleStorage, network
# import os

def deploy_simple_storage():
    # account = accounts[0]
    account = get_account()
    # account = accounts.load("freecodecamp-account")
    # account = accounts.add(config["wallet"]['from_key'])
    # print(account)
    simple_storage = SimpleStorage.deploy({"from":account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_store_value = simple_storage.retrieve()
    print(updated_store_value)



def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallet"]['from_key'])




def main():
    deploy_simple_storage()