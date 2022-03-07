// SPDX-License-Identifier: MIT
pragma solidity > 0.6.0;

contract Mine
{
    enum Allnums
    {
        zero,
        one,
        two,
        three
    }

    Allnums mynum;
    Allnums constant myfavenum = Allnums.three;

    function get() public view returns(Allnums)
    {
        return mynum;
    }

    function multiply() public pure returns(uint)
    {
        return uint(myfavenum);
    }
}