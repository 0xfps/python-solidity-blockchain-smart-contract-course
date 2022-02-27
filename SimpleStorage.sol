// SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.6.0 < 0.9.0;

contract SimpleStorage
{
    // this will get initialized to 0 
    uint256 favouriteNumber;

    function store(uint256 _favouriteNumber) public
    {
        favouriteNumber = _favouriteNumber;
    }

    function retrieve() public view returns(uint256)
    {
        return favouriteNumber + favouriteNumber;
    }
}