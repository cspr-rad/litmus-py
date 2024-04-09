import enum

from pylitmus import chain
from pylitmus import digests


class VerificationErrorType(enum.Enum):
    INVALID_BLOCK_HASH = enum.auto()


class VerificationError(Exception):
    typeof: VerificationErrorType

    def __init__(self, typeof: VerificationErrorType) -> None:
        self.typeof = typeof


def verify_block(block: chain.Block):
    print(block.hash.hex(), digests.get_digest_of_block(block.header).hex())

    if block.hash != digests.get_digest_of_block(block.header):
        raise VerificationError(VerificationErrorType.INVALID_BLOCK_HASH)


def verify_block_body(block: chain.Block):
    # TODO: recompute hash and assert equivalence.

    assert block.header.body_hash == block.header.body_hash
