from pycspr.types.node import Block

from pylitmus.verifier.blocks import validate_block
from pylitmus.verifier.blocks import validate_switch_block


def verify_block(
    block: Block,
    switch_block_of_previous_era: Block = None
) -> Block:
    """Verifies a block.

    :params block: Block to be verified.
    :params switch_block_of_previous_era: Parent switch block of block to be verified.
    
    """
    return validate_block(block, switch_block_of_previous_era)


def verify_block_at_era_end(
    block: Block,
    switch_block_of_previous_era: Block = None
) -> Block:
    """Verifies a block at the end of an era, i.e. a switch block.
    
    :params block: Block to be verified.

    """
    return validate_switch_block(block, switch_block_of_previous_era)
