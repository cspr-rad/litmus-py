from pycspr.types.node import Block
from pycspr.types.node import BlockHash

from pylitmus import cache
from pylitmus import chain


async def init_from_trusted_block_hash(block_hash: BlockHash):
    """Initialises light client from a trusted block hash.

    :param block_hash: Hash of a trusted block.

    """
    # Descend -> switch block.
    block: Block = await chain.get_switch_block_of_previous_era(block_hash)

    # Ascend -> tip.
    async for block in chain.ascend_until_tip(None, None, block):
        cache.blocks.set_block(block)
