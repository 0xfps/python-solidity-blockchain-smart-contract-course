// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage
{
    // this will get initialized to 0 
    uint256 favouriteNumber;
    bool favouriteBool;

    function store(uint256 _favouriteNumber) public returns(uint256)
    {
        favouriteNumber = _favouriteNumber;
        return favouriteNumber;
    }

    struct People
    {
        uint favouriteNumber;
        string name;
    }

    People[] public people;
    
    // creates a function that maps one unique key "string" to a value "uint256"
    mapping(string => uint256) public nameToFavouriteNumber;

    function retrieve() public view returns(uint256)
    {
        return favouriteNumber + favouriteNumber;
    }

    function addPerson(string memory _name, uint256 _favouriteNumber) public
    {
        people.push(People(_favouriteNumber, _name));
        // This is where the actual mapping is done
        nameToFavouriteNumber[_name] = _favouriteNumber;
    }
}