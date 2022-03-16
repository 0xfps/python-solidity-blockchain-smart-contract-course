from brownie import config, accounts, network, MockV3Aggregator
from web3 import Web3

DECIMALS = 18
STARTING_PRICE = 2000

# we are gonna make this a little bit more robust
def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config['wallet']['from_key'])


def deploy_mocks():
        print(f"The active network is {network.show_active()}")
        print("Deploying mocks...")

        if len(MockV3Aggregator) <= 0:
            MockV3Aggregator.deploy(DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()})
        
        print("Mocks deployed")