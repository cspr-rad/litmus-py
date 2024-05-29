import random
import typing

from pylitmus.node import Node
from pylitmus.types import Block
from pylitmus.types import BlockID


# Set of registered nodes.
_NODES: typing.List[Node] = []


async def get_block(block_id: BlockID, node_id: int = None) -> Block:
    """Queries a node for a block.
    
    :param block_id: Identifier of a trusted block.
    :returns: A matched block.
    
    """
    node: Node = _get_node()

    # TODO: handle proxy errors.
    return await node.get_block(block_id)


async def get_block_range() -> typing.Tuple[int, int]:
    """Queries a node for it's available block range.
    
    :param block_hash: Hash of a trusted block.
    :returns: A matched block.
    
    """
    node: Node = _get_node()

    return await node.get_block_range()


async def get_chain_height() -> int:
    """Queries a node for it's block height.
    
    :returns: A matched block.
    
    """
    return (await get_block_range())[1]


def register_node(host: str, rpc_port: int, sse_port: int):
    """Registers a node with network set.
    
    :param host: Host address of node.
    :param rpc_port: JSON-RPC port of node.
    :param sse_port: SSE port of node.

    """
    _NODES.append(
        Node(host, rpc_port, sse_port)
        )


def _get_node() -> Node:
    """Returns a random node proxy.
    
    """
    if not _NODES:
        raise ValueError("Invalid node set.")

    return random.choice(_NODES)
