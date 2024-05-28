import typing

from pycspr import NodeRpcProxyError
from pycspr.types.node import Block
from pycspr.types.node import BlockHash

from pylitmus import network
from pylitmus import verifier


async def get_switch_block_of_previous_era(block_hash: BlockHash) -> Block:
    """Returns switch block of previous era.
    
    :param block_hash: Hash of a trusted block.
    :returns: Generator over a set of historical blocks.

    """
    # Pull & validate block matched by ID.
    block: Block = verifier.validate_block(
        await network.get_block(block_hash)
    )

    # Descend & validate historical blocks. 
    while block.is_switch is False:
        block: Block = verifier.validate_block(
            await network.get_block(block.header.parent_hash)
        )

    # Return validated switch block.
    return verifier.validate_switch_block(block)


async def ascend_until_tip(
    block: Block,
    parent_block: Block,
    switch_block: Block
) -> typing.Generator:
    """Yields future blocks until chain tip is reached.
    
    :param block: A block from which to ascend.
    :param parent_block: Parent of the block from which to ascend.
    :param switch_block: Previous era switch block.
    :returns: Generator over a set of blocks.

    """
    if block is None and parent_block is None:
        block = parent_block = verifier.validate_switch_block(switch_block)

    # Set current chain height.
    chain_height: int = await network.get_chain_height()

    # Ascend until current chain height.
    while block.header.height < chain_height:
        try:
            block: Block = verifier.validate_block(
                await network.get_block(parent_block.height + 1),
                switch_block,
            )
        except NodeRpcProxyError as err:
            print(err)
            # TODO: define exception policy/handling.
            return
        else:
            parent_block: Block = block
            if block.is_switch:
                switch_block = block
            yield block

    # Catchup if behind.
    if block.header.height < await network.get_chain_height():
        async for block in ascend_until_tip(block, parent_block, switch_block):
            yield block
