import pycspr

from pylitmus import chain


def verify_block(
    block: chain.Block,
    parent_block: chain.Block = None,
    parent_switch_block: chain.Block = None
) -> chain.Block:
    """Verifies a block.
    
    """
    return pycspr.validate_block(block, parent_block, parent_switch_block)


def verify_switch_block(block: chain.Block) -> chain.Block:
    return pycspr.validate_block_at_era_end(block)
