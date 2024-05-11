import typing

from pycspr import NodeRpcProxyError
from pycspr.types.node import Block
from pycspr.types.node import BlockHash
from pycspr.types.node import BlockHeight
from pycspr.types.node import BlockID

from pylitmus import network
from pylitmus import verifier


async def yield_until_previous_switch_block(block_id: BlockID) -> typing.Generator:
    """Yields verified historical blocks until a switch block is reached.
    
    :param block_hash: Hash of a trusted block.
    :returns: Generator over a set of historical blocks.

    """
    block: Block = verifier.verify_block(
        await network.get_block(block_id)
    )
    while block.is_switch is False:
        yield block
        block: Block = verifier.verify_block(
            await network.get_block(block.header.parent_hash)
        )
    yield block


async def yield_until_tip(block: Block) -> typing.Generator:
    """Yields future blocks until chain tip is reached.
    
    :param block_height: Height of a block.
    :returns: Generator over a set of blocks.

    """
    parent_switch_block = parent_block = verifier.verify_block_at_era_end(block)
    while block is not None:
        try:
            block: Block = verifier.verify_block(
                await network.get_block(parent_block.height + 1),
                parent_block,
                parent_switch_block,
            )
        except NodeRpcProxyError as err:
            print(err)
            # TODO: be more specifc
            return
        else:
            yield block
            parent_block: Block = block
            if block.is_switch:
                parent_switch_block = block
