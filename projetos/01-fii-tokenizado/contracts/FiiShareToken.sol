// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/// @notice Educational token model. Not a regulated fund share registry.
contract FiiShareToken {
    string public constant name = "Simulated FII Share";
    string public constant symbol = "sFII";
    uint8 public constant decimals = 18;
    address public admin;
    bool public paused;
    mapping(address => bool) public eligible;
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    event Transfer(address indexed from, address indexed to, uint256 amount);
    event EligibilityChanged(address indexed account, bool eligible);
    event Paused(bool state);

    modifier onlyAdmin() { require(msg.sender == admin, "admin only"); _; }
    modifier live() { require(!paused, "paused"); _; }

    constructor() { admin = msg.sender; }

    function setEligible(address account, bool state) external onlyAdmin {
        eligible[account] = state;
        emit EligibilityChanged(account, state);
    }

    function setPaused(bool state) external onlyAdmin {
        paused = state;
        emit Paused(state);
    }

    function mint(address to, uint256 amount) external onlyAdmin live {
        require(eligible[to], "recipient not eligible");
        balanceOf[to] += amount;
        emit Transfer(address(0), to, amount);
    }

    function transfer(address to, uint256 amount) external live returns (bool) {
        _transfer(msg.sender, to, amount);
        return true;
    }

    function approve(address spender, uint256 amount) external live returns (bool) {
        allowance[msg.sender][spender] = amount;
        return true;
    }

    function transferFrom(address from, address to, uint256 amount) external live returns (bool) {
        uint256 allowed = allowance[from][msg.sender];
        require(allowed >= amount, "allowance exceeded");
        allowance[from][msg.sender] = allowed - amount;
        _transfer(from, to, amount);
        return true;
    }

    function _transfer(address from, address to, uint256 amount) internal {
        require(eligible[to], "recipient not eligible");
        require(balanceOf[from] >= amount, "insufficient balance");
        balanceOf[from] -= amount;
        balanceOf[to] += amount;
        emit Transfer(from, to, amount);
    }
}
