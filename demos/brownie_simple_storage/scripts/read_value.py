from brownie import accounts, config, SimpleStorage, network
import os

def read_contract():
    simple_storage = SimpleStorage[-1]
    # simple_storage.store(40, {"from": get_account()})
    print(simple_storage.retrieve())



def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallet"]['from_key'])


def main():
    read_contract()