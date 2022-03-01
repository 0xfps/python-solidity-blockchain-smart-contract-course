// SPDX-License-Identifier: MIT

pragma solidity > 0.6.0;

import "./calc.sol";

contract nums
{
    // math[] matarray;
    address mataddress;
    uint[] public arr = [1, 2, 3, 4, 5];

    constructor()
    {
        math newmath = new math();
        // matarray.push(newmath);
        mataddress = address(newmath);
    }

    function performsub() public view returns(uint)
    {
        // math domath = math(address(matarray[0]));

        //the return value of line 14 is yet unknown but is to be casted into address before use.
        math domath = math(mataddress);
        // domath.add([1,2,3,4,5,6]);
        return domath.sub(11, 2);
    }

    function performadd() public view returns(uint)
    {
        // math domath = math(address(matarray[0]));

        //the return value of line 14 is yet unknown but is to be casted into address before use.
        math domath = math(mataddress);
        // domath.add([1,2,3,4,5,6]);
        return domath.add(arr);
    }
}
