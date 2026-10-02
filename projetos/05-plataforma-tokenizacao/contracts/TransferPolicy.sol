// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/// @notice Toy policy gate for a sandbox token transfer.
contract TransferPolicy {
    address public admin;
    bool public paused;
    mapping(address => bool) public eligible;
    mapping(address => uint256) public balance;
    event EligibilitySet(address indexed account, bool allowed);
    event Transfer(address indexed from, address indexed to, uint256 amount);

    constructor() { admin = msg.sender; }
    modifier onlyAdmin() { require(msg.sender == admin, "admin only"); _; }

    function setEligible(address account, bool allowed) external onlyAdmin {
        eligible[account] = allowed;
        emit EligibilitySet(account, allowed);
    }

    function setPaused(bool state) external onlyAdmin { paused = state; }

    function mint(address to, uint256 amount) external onlyAdmin {
        require(!paused && eligible[to], "not permitted");
        balance[to] += amount;
        emit Transfer(address(0), to, amount);
    }

    function transfer(address to, uint256 amount) external {
        require(!paused && eligible[msg.sender] && eligible[to], "not permitted");
        require(balance[msg.sender] >= amount, "insufficient balance");
        balance[msg.sender] -= amount;
        balance[to] += amount;
        emit Transfer(msg.sender, to, amount);
    }
}
