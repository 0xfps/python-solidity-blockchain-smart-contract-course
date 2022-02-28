// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;


contract NestedMapping {
    // Nested mapping (mapping from address to another mapping)
    mapping(string => mapping(uint => int)) public nested;

    function set(
        string memory _addr1,
        uint _i,
        int _boo
    ) public {
        nested[_addr1][_i] = _boo;
    }

    function remove(string memory _addr1, uint _i) public {
        delete nested[_addr1][_i];
    }
}
