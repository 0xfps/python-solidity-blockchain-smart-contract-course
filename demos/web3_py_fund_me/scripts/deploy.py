from brownie import config, network, FundMe, accounts

def deploy():
    account = get_account()

    dep = FundMe.deploy({"from": account}, publish_source=True)
    print("Deployed at ", dep.address)



def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config['wallet']['from_key'])



def main():
    deploy()