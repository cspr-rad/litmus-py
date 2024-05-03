from pylitmus.kernel import Kernel
from pycspr.types.node import BlockHash
from pycspr import NodeRpcClient
from pycspr import NodeRpcConnectionInfo
from pycspr import NodeSseClient
from pycspr import NodeSseConnectionInfo


def create_kernel(block_id: BlockHash):
    return Kernel(block_id)


def create_node_rpc_client(
    host: str,
    rpc_port: int,
) -> NodeRpcClient:
    return NodeRpcClient(
        NodeRpcConnectionInfo(host, rpc_port)
    )


def create_node_sse_client(
    host: str,
    sse_port: int,
    rpc_port: int,
) -> NodeSseClient:
    return NodeSseClient(
        NodeSseConnectionInfo(host, sse_port, rpc_port)
    )
