from pycspr.types.node import Block

from pylitmus import cache
from pylitmus import chain


async def init_from_trusted_block_hash(block_hash: chain.BlockHash):
    """Initialises light client from a trusted block hash.

    :param block_hash: Hash of trusted block.

    """
    # Descend -> switch block.
    block: Block = chain.get_previous_era_switch_block(block_hash):

    # Ascend -> tip.
    async for block in chain.ascend_until_tip(None, None, block):
        cache.blocks.set_block(block)
