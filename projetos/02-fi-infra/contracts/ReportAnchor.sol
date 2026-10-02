// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/// @notice Stores hashes of simulated risk reports; does not validate report truth.
contract ReportAnchor {
    address public immutable reporter;
    mapping(bytes32 => uint64) public anchoredAt;
    event Anchored(bytes32 indexed reportHash, uint64 timestamp);

    constructor() { reporter = msg.sender; }

    function anchor(bytes32 reportHash) external {
        require(msg.sender == reporter, "reporter only");
        require(anchoredAt[reportHash] == 0, "already anchored");
        anchoredAt[reportHash] = uint64(block.timestamp);
        emit Anchored(reportHash, uint64(block.timestamp));
    }
}
