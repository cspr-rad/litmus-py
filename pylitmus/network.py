import random
import typing

from pycspr.types.node import Block
from pycspr.types.node import BlockID

from pylitmus.node import Node


# Set of registered nodes.
_NODES: typing.List[Node] = []


async def get_block(block_id: BlockID) -> Block:
    """Queries a node for a block.
    
    :param block_id: Identifier of a trusted block.
    :returns: A matched block.
    
    """
    node: Node = _get_node()        

    return await node.get_block(block_id)


def register_node(host: str, rpc_port: int, sse_port: int):
    """Registers a node with network set.
    
    :param host: Host address of node.
    :param rpc_port: JSON-RPC port of node.
    :param sse_port: SSE port of node.

    """
    _NODES.append(
        Node(host, rpc_port, sse_port)
        )


def _get_node(node_id: int = None) -> Node:
    """Returns either a specific or a random node proxy.
    
    """
    if not _NODES:
        raise ValueError("Invalid node set.")
    if node_id is not None and node_id >= len(_NODES):
        raise ValueError("Invalid node identifier.")

    return random.choice(_NODES) if node_id is None else _NODES[node_id]
