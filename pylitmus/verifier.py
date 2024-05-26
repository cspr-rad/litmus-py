import enum

import pycspr

from pylitmus import chain


# class InvalidBlockExceptionType(enum.Enum):
#     """Enumeration over set of invalid block exception types.
    
#     """
#     ExpectedSwitchBlock = enum.auto()
#     NotFound = enum.auto()
#     InvalidFinalitySignature = enum.auto()
#     InvalidHash = enum.auto()
#     InvalidParent = enum.auto()
#     InvalidProposer = enum.auto()
#     InsufficientFinalitySignatureWeight = enum.auto()


def verify_block(
    block: chain.Block,
    parent_block: chain.Block = None,
    parent_switch_block: chain.Block = None
) -> chain.Block:
    """Verifies block data.

    :params block: Block to be verified.
    :params parent_block: Parent of block to be verified.
    :params parent_switch_block: Parent switch block of block to be verified.
    
    """
    return pycspr.validate_block(block, parent_block, parent_switch_block)


def verify_block_at_era_end(
    block: chain.Block,
    parent_block: chain.Block = None,
    parent_switch_block: chain.Block = None
) -> chain.Block:
    """Verifies block data at the end of an era.
    
    :params block: Block to be verified.

        """
    return pycspr.validate_block_at_era_end(block)
