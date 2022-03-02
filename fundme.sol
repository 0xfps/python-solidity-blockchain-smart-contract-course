// SPDX-License-Identifier: MIT

pragma solidity >= 0.6.0 < 0.9.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe
{
    mapping (address => uint256) public addressToAmountFunded;
    address public owner;

    constructor()
    {
        owner = msg.sender;
    }

    //this contract should be able to accept some type of payment
    function fund() public payable
    {
        //$50
        //Threshhold
        uint256 minimumUSD = 50 * 10 ** 18;

        require(getConversionRate(msg.value) >= minimumUSD, "You need to spend more ETH");

        addressToAmountFunded[msg.sender] += msg.value;
    }

    function getVersion() public view returns(uint256)
    {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(address(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e));
        return priceFeed.version();
    }

    function getPrice() public view returns(uint256)
    {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(address(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e));
        (, int256 answer, , ,) = priceFeed.latestRoundData();

        return uint256(answer * 10000000000); //to get a wei -- standard lowest eth
        //2637915105190000000000
    }

    
    // function getConversionRate(uint ethAmount) public view returns(uint256)
    function getConversionRate(uint ethAmount) public view returns(uint256)
    {
        uint256 ethPrice = getPrice(); //wei
        uint256 ethAmountInUSD = (ethAmount * ethPrice) / 1000000000000000000;
        return ethAmountInUSD;
    }

    modifier onlyowner
    {
        require(msg.sender == owner); 
        _;
    }

    //function to withdraw some funds
    function withdraw() payable public onlyowner
    {
        payable(msg.sender).transfer(address(this).balance);
    }
}
