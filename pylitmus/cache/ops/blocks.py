import enum
import json

import pycspr

from pylitmus.cache.keys import blocks as keys
from pylitmus.cache.model import StorePartition
from pylitmus.cache.stores import get_store
from pylitmus.chain import Block
from pylitmus.chain import BlockHash
from pylitmus.chain import BlockID


# Cache partition.
_PARTITION = StorePartition.BLOCKS


class _COLLECTIONS(enum.Enum):
    """Enumeration over set of partition collection.
    
    """
    BLOCKS = "block"


def get_count_of_blocks(era_id: int = None) -> int:
    """Decaches a verified block.

    :param era_id: Era identifier.
    :returns: Verified block information.

    """
    with get_store(StorePartition.BLOCKS) as store:
        return store.get_count(
            keys.count_of_self(era_id)
        )


def get_block(block_id: BlockID) -> bytes:
    """Decaches a verified block.

    :param block_id: Block identifier.
    :returns: Verified block information.

    """
    def _get_key():
        if isinstance(block_id, bytes):
            return keys.from_hash(block_id)
        elif isinstance(block_id, int):
            return keys.from_height(block_id)
        else:
            raise ValueError("Unrecognized block id")
    
    with get_store(StorePartition.BLOCKS) as store:
        return store.get_one_from_many(_get_key())


def get_block_by_parent_hash(block_id: BlockHash) -> bytes:
    """Decaches a verified block by it's parent hash.

    :param block_id: Parent block identifier.
    :returns: Verified block information.

    """
    with get_store(StorePartition.BLOCKS) as store:
        return store.get_one_from_many(
            keys.from_parent_hash(block_id)
        )


def get_blocks_by_era(era_id: int) -> bytes:
    """Decaches a verified block.

    :param era_id: Era identifier.
    :returns: Verified block information.

    """
    with get_store(StorePartition.BLOCKS) as store:
        return store.get_many(
            keys.from_era(era_id)
        )


def get_era_switch_block(era_id: int) -> bytes:
    """Decaches a verified switch block.

    :param era_id: Era identifier.
    :returns: Verified switch block information.

    """
    with get_store(StorePartition.BLOCKS) as store:
        return store.get_many(
            keys.from_era_at_switch(era_id)
        )


def set_block(block: Block) -> str:
    """Encaches a verified block.

    :param block: Block data to be cached.
    :returns: Cache key.

    """
    with get_store(StorePartition.BLOCKS) as store:
        return store.set_one_singleton(
            keys.from_self(block),
            json.dumps(pycspr.to_json(block)),
        )
