// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/// @notice Demonstration log for fictitious capital calls; not a fund ledger.
contract CapitalCallLog {
    address public immutable operator;
    uint256 public nextId = 1;
    struct Call { bytes32 projectId; uint128 amount; uint64 dueDate; }
    mapping(uint256 => Call) public calls;
    event CallCreated(uint256 indexed id, bytes32 indexed projectId, uint256 amount, uint64 dueDate);

    constructor() { operator = msg.sender; }

    function create(bytes32 projectId, uint128 amount, uint64 dueDate) external returns (uint256 id) {
        require(msg.sender == operator, "operator only");
        require(amount > 0 && dueDate > block.timestamp, "invalid call");
        id = nextId++;
        calls[id] = Call(projectId, amount, dueDate);
        emit CallCreated(id, projectId, amount, dueDate);
    }
}
