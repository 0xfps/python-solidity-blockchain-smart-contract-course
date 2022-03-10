from brownie import SimpleStorage, accounts

def test_deploy():
    # Arrange
    account = accounts[0]
    # account = accounts.load("freecodecamp-account")
    # account = accounts.add(config["wallet"]['from_key'])

    # Act
    simple_storage = SimpleStorage.deploy({"from":account})
    starting_value = simple_storage.retrieve()
    expected = 0

    # Assert
    assert starting_value == expected 



def test_updating_storage():
    # Arrange
    account = accounts[0]

    # Act
    simple_storage = SimpleStorage.deploy({"from":account})
    transaction = simple_storage.store(15, {"from": account})
    starting_value = simple_storage.retrieve()
    expected = 30

    # Assert
    assert starting_value == expected