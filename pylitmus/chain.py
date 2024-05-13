import typing

from pycspr import NodeRpcProxyError
from pycspr.types.node import Block
from pycspr.types.node import BlockHash
from pycspr.types.node import BlockHeight
from pycspr.types.node import BlockID

from pylitmus import network
from pylitmus import verifier


async def descend_until_switch_block(block_id: BlockID) -> typing.Generator:
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

    yield verifier.verify_block_at_era_end(block)


async def ascend_until_tip(
    block: Block,
    parent_block: Block,
    switch_block: Block
) -> typing.Generator:
    """Yields future blocks until chain tip is reached.
    
    :param block_height: Height of a block.
    :returns: Generator over a set of blocks.

    """
    if block is None and parent_block is None:
        block = parent_block = verifier.verify_block_at_era_end(switch_block)

    chain_height: int = await network.get_chain_height()
    while block.header.height < chain_height:
        try:
            block: Block = verifier.verify_block(
                await network.get_block(parent_block.height + 1),
                parent_block,
                switch_block,
            )
        except NodeRpcProxyError as err:
            print(err)
            # TODO: define exception policy/handling.
            return
        else:
            yield block
            parent_block: Block = block
            if block.is_switch:
                switch_block = block

    if block.header.height < await network.get_chain_height():
        async for block in ascend_until_tip(block, parent_block, switch_block):
            yield block
