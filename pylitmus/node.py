from pycspr.types.node import Block
from pycspr.types.node import BlockHash

from pylitmus import factory


class Node():
    def __init__(self, host: str, rpc_port: int, sse_port: int) -> None:
        """Instance constructor.
        
        :param host: Host address of node.
        :param rpc_port: JSON-RPC port of node.
        :param sse_port: SSE port of node.

        """
        self.rpc_client = factory.create_node_rpc_client(host, rpc_port)
        self.sse_client = factory.create_node_sse_client(host, sse_port, rpc_port)


    async def get_block(self, block_hash: BlockHash) -> Block:
        """Queries a node for a block.
        
        :param block_hash: Hash of a trusted block.
        :returns: A matched block.
        
        """
        return await self.rpc_client.get_block(block_hash)
