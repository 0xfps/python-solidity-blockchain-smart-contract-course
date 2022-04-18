// SPDX-License-Identifier: MIT

pragma solidity >0.6.0;

/*
	A simple contract to take two numbers, sum both and bring out output
*/

contract Add
{
    uint256 total;

    function getnums(uint256 num1, uint256 num2) public
    {
        total = num1 + num2;
    }

    function gettotal() public view returns(uint256)
    {
        return total;
    }
}
