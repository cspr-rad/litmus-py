import typing

from pycspr import NodeRpcClient
from pycspr import NodeRpcConnectionInfo
from pycspr import NodeSseClient
from pycspr import NodeSseConnectionInfo
from pylitmus.types import Block
from pylitmus.types import BlockHash


class Node():
    """Wraps interaction with a remote node's API surface.
    
    """
    def __init__(self, host: str, rpc_port: int, sse_port: int) -> None:
        """Instance constructor.
        
        :param host: Host address of node.
        :param rpc_port: JSON-RPC port of node.
        :param sse_port: SSE port of node.

        """
        self.rpc_client = NodeRpcClient(
            NodeRpcConnectionInfo(host, rpc_port)
        )
        self.sse_client = NodeSseClient(
            NodeSseConnectionInfo(host, sse_port, rpc_port)
        )

    async def get_block(self, block_hash: BlockHash) -> Block:
        """Queries a node for a block.
        
        :param block_hash: Hash of a trusted block.
        :returns: A matched block.
        
        """
        return await self.rpc_client.get_block(block_hash)
    
    async def get_block_range(self) -> typing.Tuple[int, int]:
        """Queries a node for it's available block range.
        
        :param block_hash: Hash of a trusted block.
        :returns: A matched block.
        
        """
        return await self.rpc_client.get_block_range()
