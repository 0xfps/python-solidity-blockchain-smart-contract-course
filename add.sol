//SPDX-License-Identifier: UNLICENSED

pragma solidity > 0.6.0;

/*
	A simple contract to take two numbers, sum both and bring out output
*/

contract Add
{
    uint total;

    function getnums(uint num1, uint num2) public
    {
        total = num1 + num2;
    }

    function gettotal() public view returns(uint)
    {
        return total;
    }
}
