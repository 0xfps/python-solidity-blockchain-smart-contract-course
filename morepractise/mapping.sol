// SPDX-License-Identifier: MIT
pragma solidity ^0.5.0;
contract LedgerBalance {
   mapping(address => uint) public balances;

   function updateBalance(uint newBalance) public {
      balances[msg.sender] = newBalance;
   }
}
contract Updater {
   function updateBalance() public returns (uint) {
      LedgerBalance ledgerBalance;
      ledgerBalance.updateBalance(10);
      return ledgerBalance.balances(address(this));
   }
}