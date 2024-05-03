from pycspr.types.node import BlockHash
# from pylitmus.types import Kernel


def on_block_finalisation(block_id: BlockHash):
    print(block_id)

