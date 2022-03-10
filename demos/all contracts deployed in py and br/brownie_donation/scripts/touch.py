from brownie import Donation, network, accounts, config

def deploy():
    account = accounts.add(config['wallet']['from_key'])
    touch_var = Donation[-1]
    print("Current length ", str(touch_var.See_Length()))
    touch_var.Donate(5000, {"from": account})
    touch_var.Donate(3000, {"from": account})
    touch_var.Donate(1000, {"from": account})
    print("Deployed")
    print("New length ", str(touch_var.See_Length()))

def main():
    deploy()