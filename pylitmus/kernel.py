import pycspr

from pylitmus import cache
from pylitmus import cache1
from pylitmus import network
from pylitmus import chain
from pylitmus import verifier


async def init_from_trusted_block_height(block_height: chain.BlockHeight):
    """Initialises light client from a trusted block height.

    :param block_height: Height of trusted block.

    """
    try:
        block: chain.Block = await network.get_block(block_height)
    except Exception as err:
        # TODO: handle exception
        print(err)
    else:
        return await init_from_trusted_block_hash(block.hash)


async def init_from_trusted_block_hash(block_hash: chain.BlockHash):
    """Initialises light client from a trusted block hash.

    :param block_hash: Hash of trusted block.

    """
    # Initialise trusted cache.
    await cache.init()

    # Descend chain -> most recent valid switch block.
    async for block in chain.yield_until_previous_switch_block(block_hash):
        pass

    # Ascend chain -> tip.
    async for block in chain.yield_until_tip(block):
        cache1.blocks.set_verified_block(block)

    # Bind to SSE event channel and keep cache fresh.
    # TODO
