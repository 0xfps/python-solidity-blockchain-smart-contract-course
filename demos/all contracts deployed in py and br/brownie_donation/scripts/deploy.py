from brownie import Donation, network, accounts, config

def deploy():
    account = accounts.add(config['wallet']['from_key'])
    deploy_var = Donation.deploy({"from": account})
    print("Deployed")

def main():
    deploy()