from pycspr import NodeRpcClient
from pycspr import NodeRpcConnectionInfo
from pycspr import NodeSseClient
from pycspr import NodeSseConnectionInfo


def create_node_rpc_client(
    host: str,
    rpc_port: int,
) -> NodeRpcClient:
    """Instantiate & return a node JSON-RPC client.
    
    :params host: Host address of target node.
    :params rpc_port: JSON-RPC port of target node.
    :returns: A JSON-RPC node client.

    """
    return NodeRpcClient(
        NodeRpcConnectionInfo(host, rpc_port)
    )


def create_node_sse_client(
    host: str,
    sse_port: int,
    rpc_port: int,
) -> NodeSseClient:
    """Instantiate & return a node SSE client.
    
    :params host: Host address of target node.
    :params sse_port: SSE port of target node.
    :params rpc_port: JSON-RPC port of target node.
    :returns: An SSE node client.

    """
    return NodeSseClient(
        NodeSseConnectionInfo(host, sse_port, rpc_port)
    )
