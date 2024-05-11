import random
import typing

from pycspr.types.node import Block
from pycspr.types.node import BlockID

from pylitmus.node import Node


# Set of registered nodes.
_NODES: typing.List[Node] = []


async def get_block(block_id: BlockID, node_id: int = None) -> Block:
    """Queries a node for a block.
    
    :param block_id: Identifier of a trusted block.
    :param node_id: Identifier of a registered node.
    :returns: A matched block.
    
    """
    return await get_node(node_id).get_block(block_id)


async def get_block_range(node_id: int = None) -> typing.Tuple[int, int]:
    """Queries a node for it's available block range.
    
    :param block_hash: Hash of a trusted block.
    :returns: A matched block.
    
    """
    return await get_node(node_id).get_block_range()


def get_node(node_id: int = None) -> Node:
    """Returns either a specific or a random node proxy.
    
    """
    if not _NODES:
        raise ValueError("Invalid node set.")
    if node_id is not None and (node_id < 0 or node_id >= len(_NODES) - 1):
        raise ValueError("Invalid node identifier.")

    return random.choice(_NODES) if node_id is None else _NODES[node_id]


def register_node(host: str, rpc_port: int, sse_port: int):
    """Registers a node with network set.
    
    :param host: Host address of node.
    :param rpc_port: JSON-RPC port of node.
    :param sse_port: SSE port of node.

    """
    _NODES.append(
        Node(host, rpc_port, sse_port)
        )
