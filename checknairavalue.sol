
// SPDX-License-Identifier: MIT

pragma solidity > 0.6.0;

//A function that converts and evaluates the conversion to nara

contract changeToNaira
{
    mapping(string => uint) sender;

    struct notebook
    {
        string moneyman;
        uint money;
    }

    notebook[] mynote;

    uint public length = 0;

    function addlength() internal
    {
        length += 1;
    }

    function sendMoney(string memory moneySender, uint amount) public
    {
        require(amount * 100 < 600, "Too small, the minimm you can send is N6");
        mynote.push(notebook(moneySender, amount*100));
        sender[moneySender] = amount * 100;
        addlength();
    }

    function retrieve(string memory person) public view returns(uint)
    {
        return sender[person];
    }

    function returnLength() public view returns(uint256)
    {
        return length;
    }
}
