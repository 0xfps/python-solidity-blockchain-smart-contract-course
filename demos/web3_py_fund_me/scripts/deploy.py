from brownie import config, network, FundMe, MockV3Aggregator, accounts
from scripts.helpful_scripts import get_account, deploy_mocks
from web3 import Web3

def deploy():
    account = get_account()

    if network.show_active() != "development":
        price_feed_address = config['networks'][network.show_active()]['eth_usd_price_feed']
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    

    dep = FundMe.deploy(price_feed_address, {"from": account}, publish_source=config["networks"][network.show_active()]["verify"])
    print("Deployed at ", dep.address)



def main():
    deploy()