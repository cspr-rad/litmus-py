from pycspr.types.node import Block

from pylitmus.verifier.blocks import validate_block
from pylitmus.verifier.blocks import validate_switch_block


def verify_block(
    block: Block,
    parent_block: Block = None,
    parent_switch_block: Block = None
) -> Block:
    """Verifies a block.

    :params block: Block to be verified.
    :params parent_block: Parent of block to be verified.
    :params parent_switch_block: Parent switch block of block to be verified.
    
    """
    return validate_block(block, parent_block, parent_switch_block)


def verify_block_at_era_end(
    block: Block,
    parent_block: Block = None,
    parent_switch_block: Block = None
) -> Block:
    """Verifies a block at the end of an era, i.e. a switch block.
    
    :params block: Block to be verified.

    """
    return validate_switch_block(block)
