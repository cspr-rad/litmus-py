from pycspr.types.node.rpc import Block
from pycspr.types.node.rpc import BlockHash
from pycspr.types.node.rpc import BlockHeader
from pycspr.types.node.rpc import BlockHeight
from pylitmus import cache
from pylitmus import node


def get_block_by_hash(block_hash: BlockHash) -> Block:
    block: Block = cache.get_block_by_hash(block_hash)
    if block is None:
        raise ValueError("TODO: call network")

    return block


def get_previous_switch_block(block_hash: BlockHash):
    block: Block = cache.get_block_by_hash(block_hash)
    if block is None:
        raise ValueError("Block not found")
    elif block.header.era_end is not None:
        return block
    else:
        return get_previous_switch_block(block.header.parent_hash)


def get_next_switch_block(block_height: BlockHeight):
    block: Block = cache.get_block_by_height(block_height)
    if block is None:
        raise ValueError("Block not found")
    elif block.header.era_end is not None:
        return block
    else:
        return get_next_switch_block(block_height + 1)


async def yield_until_switch_block(block_hash: BlockHash):
    block: Block = await node.get_block(block_hash)
    if block is None:
        raise Exception(f"Invalid block hash: {block_hash.hex()}")

    while block.is_switch_block is False:
        yield block

        block: Block = await node.get_block(block.header.parent_hash)
        if block is None:
            raise Exception(f"Invalid block hash: {block_hash.hex()}")

    yield block
