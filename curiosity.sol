// SPDX-License-Identifier: MIT
pragma solidity >= 0.6.0 < 0.9.0;

// importing the SimpleStorage.sol contract.
// We can have two contracts in the same file.
import "./SimpleStorage.sol";

contract StorageFactory
{
    SimpleStorage[] public simpleStorageArray;

    function createSimpleStorageContract() public
    {
        //create an object of type SimpleStorage
        SimpleStorage simpleStorage = new SimpleStorage();
        simpleStorageArray.push(simpleStorage);
    }

    uint number = 0;

    function sfStore(uint256 _simpleStorageNumber) public
    {
        //Address
        // A.B.I
        uint256 _simpleStorageIndex;
        _simpleStorageIndex = number;
        SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        simpleStorage.store(_simpleStorageNumber);
        number += 1;
    }

    function sfGet(uint256 _simpleStorageIndex) public view returns(uint256)
    {
        SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        return simpleStorage.retrieve();
    }
}
