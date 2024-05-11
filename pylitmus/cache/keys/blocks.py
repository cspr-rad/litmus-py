import enum

from pylitmus.cache.keys.utils import get_key
from pylitmus.chain import Block


class _COLLECTIONS(enum.Enum):
    """Enumeration over set of partition collection.
    
    """
    BLOCKS = "block"


def from_self(block: Block) -> str:
    return get_key(
        [
            _COLLECTIONS.BLOCKS.value,
        ],
        [
            # Chain era.
            str(block.header.era_id).zfill(12),
            # Block height.
            str(block.header.height).zfill(12),
            # Block hash.
            block.hash.hex(),
            # Block type.
            int(block.is_switch),
            # Block parent hash.
            block.header.parent_hash.hex(),
            # Chain state root hash.
            block.header.state_root.hex(),
            # Chain protocol version.
            str(block.header.protocol_version),
        ]
    )


def from_hash(block_hash: bytes) -> str:
    return get_key(
        [
            _COLLECTIONS.BLOCKS.value,
        ],
        [
            # Chain era.
            "*",
            # Block height.
            "*",
            # Block hash.
            block_hash.hex(),
            # Block type.
            "*",
            # Block parent hash.
            "*",
            # Chain state root hash.
            "*",
            # Chain protocol version.
            "*",
        ]
    )


def from_height(block_height: int) -> str:
    return get_key(
        [
            _COLLECTIONS.BLOCKS.value,
        ],
        [
            # Chain era.
            "*",
            # Block height.
            str(block_height).zfill(12),
            # Block hash.
            "*",
            # Block type.
            "*",
            # Block parent hash.
            "*",
            # Chain state root hash.
            "*",
            # Chain protocol version.
            "*",
        ]
    )


def from_parent_hash(parent_hash: bytes) -> str:
    return get_key(
        [
            _COLLECTIONS.BLOCKS.value,
        ],
        [
            # Chain era.
            "*",
            # Block height.
            "*",
            # Block hash.
            "*",
            # Block type.
            "*",
            # Block parent hash.
            parent_hash.hex(),
            # Chain state root hash.
            "*",
            # Chain protocol version.
            "*",
        ]
    )


def from_era(era_id: int) -> str:
    return get_key(
        [
            _COLLECTIONS.BLOCKS.value,
        ],
        [
            # Chain era.
            str(era_id).zfill(12),
            # Block height.
            "*",
            # Block hash.
            "*",
            # Block type.
            "*",
            # Block parent hash.
            "*",
            # Chain state root hash.
            "*",
            # Chain protocol version.
            "*",
        ]
    )


def count_of_self(era_id: int = None) -> str:
    return get_key(
        [
            _COLLECTIONS.BLOCKS.value,
        ],
        [
            # Chain era.
            "*" if era_id is None else str(era_id).zfill(12),
            # Block height.
            "*",
            # Block hash.
            "*",
            # Block type.
            "*",
            # Block parent hash.
            "*",
            # Chain state root hash.
            "*",
            # Chain protocol version.
            "*",
        ]
    )