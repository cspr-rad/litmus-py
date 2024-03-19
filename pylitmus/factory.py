from pylitmus.kernel import Kernel
from pylitmus.types import BlockHash


def create_kernel(block_id: BlockHash):
    return Kernel(block_id)
