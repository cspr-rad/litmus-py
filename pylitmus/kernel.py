from pylitmus import cache
from pylitmus import chain
from pylitmus.types import Block
from pylitmus.types import BlockInfo
from pylitmus.types import BlockHash
from pylitmus.types import EraInfo


async def init_from_trusted_block_hash(block_hash: BlockHash):
    """Initialises light client from a trusted block hash.

    :param block_hash: Hash of a trusted block.

    """
    # Descend -> switch block & encache.
    block: Block = await chain.get_switch_block_of_previous_era(block_hash)
    cache.era_info.set(EraInfo.from_block(block))

    # Ascend -> tip & encache.
    async for block in chain.ascend_until_tip(None, None, block):
        cache.block.set(block)
        cache.block_info.set(BlockInfo.from_block(block))
        if block.is_switch:
            # print(cache.era_info.get(block.header.era_id))
            cache.era_info.set(EraInfo.from_block(block))
