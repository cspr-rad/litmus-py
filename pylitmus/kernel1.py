from pylitmus import cache
from pylitmus import factory
from pylitmus import node
from pylitmus import chain
from pylitmus import verifier


async def init_from_trusted_block_height(
    block_height: chain.BlockHeight,
    address_of_node: str,
    rpc_port_of_node: int,
    sse_port_of_node: int,
):
    rpc_client = factory.create_node_rpc_client(address_of_node, rpc_port_of_node)

    try:
        block: chain.Block = await rpc_client.get_block(block_height)
    except Exception as err:
        # TODO: handle exception
        print(err)
    else:
        await init_from_trusted_block_hash(
            block.hash,
            address_of_node,
            rpc_port_of_node,
            sse_port_of_node
        )


async def init_from_trusted_block_hash(
    block_hash: chain.BlockHash,
    address_of_node: str,
    rpc_port_of_node: int,
    sse_port_of_node: int,
):
    # Initialise internal components.
    node.init(address_of_node, rpc_port_of_node, sse_port_of_node)
    cache.init()

    # Verifiably descend chain to first switch block.
    async for block in chain.yield_until_switch_block(block_hash):
        try:
            verifier.verify_block(block)
        except verifier.VerificationError as err:
            raise err
        else:
            cache.set_block(block)

    # Verifiably ascend chain to tip.
