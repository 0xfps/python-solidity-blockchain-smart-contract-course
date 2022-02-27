//SPDX-License-Identifier: MIT

//same code but it returns the length of the items in the struct now.

pragma solidity > 0.6.0;

contract assign
{
    struct People
    {
        string name;
        uint age;
        string favouriteColor;
    }

    People[] person;

    //mapping the name to the age 
    mapping (string => uint) namesake;
    uint public lengthofpeople;

    function addaperson(string memory _name, uint _age, string memory _fav) public
    {
        person.push(People(_name, _age, _fav));

        //this part of the code is actually assigned and will be printed
        // namesake[_name] = person.length;
        lengthofpeople = person.length;
    }
}
