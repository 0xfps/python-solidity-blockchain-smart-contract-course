// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

contract Donation
{
    // mapping the address to the amount donated by any donor
    mapping(address => uint) donormap;

    // initiating the total amount kept to 0
    uint totalamount;

    // A structure of all donors
    struct Donors
    {
        address addr;
        uint amount;
    }

    Donors[] donors;

    // Function that when onclick donates some amount of money to the
    function Donate(uint cash) public
    {
        donormap[msg.sender] = cash;
        totalamount += cash;
        donors.push(Donors(msg.sender, cash));
    }

    // function that returns the total amount in the box
    function View_Funds() view public returns (uint)
    {
        return totalamount;
    }


    function See_Length() public view returns(uint)
    {
        return donors.length;
    }


    // function that returns the address of the at an index
    function View_Donor_Index(uint index) public view returns(address)
    {
        require(index < See_Length(), "This index is not available.");
        return donors[index].addr;
    }

    // function that returns the address of the at an index
    function View_Index_Amount(uint index) public view returns(uint)
    {
        require(index < See_Length(), "This index is not available.");
        address thisguy = donors[index].addr;
        return donormap[thisguy];
    }


    // function that displays the amount sent by a sender
    function View_Amount_Sent(address _a) public view returns(uint)
    {
        return donormap[_a];
    }
}