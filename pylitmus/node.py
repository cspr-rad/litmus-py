import typing

from pycspr import NodeRpcClient
from pycspr import NodeRpcConnectionInfo
from pycspr import NodeSseClient
from pycspr import NodeSseConnectionInfo

from pycspr.types.node.rpc import Block
from pycspr.types.node.rpc import BlockHash
from pycspr.types.node.rpc import BlockHeight

from pylitmus import factory


_RPC_CLIENT: NodeRpcClient = None
_SSE_CLIENT: NodeSseClient = None


def init(host: str, rpc_port: int, sse_port: int):
    global _RPC_CLIENT
    global _SSE_CLIENT

    _RPC_CLIENT = factory.create_node_rpc_client(host, rpc_port)
    _SSE_CLIENT = factory.create_node_sse_client(host, sse_port, rpc_port)


async def get_block(block_hash: BlockHash) -> Block:
    return await _RPC_CLIENT.get_block(block_hash)
