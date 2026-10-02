// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/// @notice Commits to a synthetic data batch; no proof of legal validity or ownership.
contract BatchCommitment {
    address public immutable submitter;
    mapping(bytes32 => uint64) public committedAt;
    event BatchCommitted(bytes32 indexed root, uint64 timestamp, uint32 itemCount);

    constructor() { submitter = msg.sender; }

    function commit(bytes32 root, uint32 itemCount) external {
        require(msg.sender == submitter, "submitter only");
        require(root != bytes32(0) && itemCount > 0, "invalid batch");
        require(committedAt[root] == 0, "duplicate root");
        committedAt[root] = uint64(block.timestamp);
        emit BatchCommitted(root, uint64(block.timestamp), itemCount);
    }
}
