from pylitmus import cache
from pylitmus import chain
from pylitmus import network


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
    # Descend to most recent valid switch block.
    async for block in chain.descend_until_switch_block(block_hash):
        pass

    # Ascend to tip.
    async for block in chain.ascend_until_tip(None, None, block):
        cache.blocks.set_block(block)
