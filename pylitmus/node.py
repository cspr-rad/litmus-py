from pycspr import NodeRpcClient
from pycspr import NodeRpcConnectionInfo
from pycspr import NodeSseClient
from pycspr import NodeSseConnectionInfo
from pycspr.types.node import Block
from pycspr.types.node import BlockHash


class Node():
    """Wraps interaction with a remote node's API surface.
    
    """
    def __init__(self, host: str, rpc_port: int, sse_port: int) -> None:
        """Instance constructor.
        
        :param host: Host address of node.
        :param rpc_port: JSON-RPC port of node.
        :param sse_port: SSE port of node.

        """
        self.rpc_client = _create_rpc_client(host, rpc_port)
        self.sse_client = _create_sse_client(host, sse_port, rpc_port)

    async def get_block(self, block_hash: BlockHash) -> Block:
        """Queries a node for a block.
        
        :param block_hash: Hash of a trusted block.
        :returns: A matched block.
        
        """
        return await self.rpc_client.get_block(block_hash)


def _create_rpc_client(host: str, rpc_port: int) -> NodeRpcClient:
    """Instantiate & return a node JSON-RPC client.
    
    """
    return NodeRpcClient(
        NodeRpcConnectionInfo(host, rpc_port)
    )


def _create_sse_client(host: str, sse_port: int, rpc_port: int) -> NodeSseClient:
    """Instantiate & return a node SSE client.
    
    """
    return NodeSseClient(
        NodeSseConnectionInfo(host, sse_port, rpc_port)
    )
