// SPDX-License-Identifier: MIT

pragma solidity > 0.6.0;

//this code does basic math.
contract math
{

    function add(uint[] memory num) public pure returns(uint)
    {
        uint sum;

        for(uint i = 0; i < num.length; i++)
        {
            sum += num[i];
        }

        return sum;
    }

    function sub(uint a, uint b) public pure returns(uint)
    {
        return a - b;
    }

    function div(uint a, uint b) public pure returns(uint)
    {
        return a / b;
    }

    function mul(uint[] memory nums) public pure returns(uint)
    {
        uint pro;

        for(uint i = 0; i < nums.length; i++)
        {
            pro += nums[i];
        }

        return pro;
    }
}
