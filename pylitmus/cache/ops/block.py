import enum
import json

import pycspr

from pylitmus.cache.keys import block as ckey
from pylitmus.cache.model import Partition
from pylitmus.cache.stores import get_store
from pylitmus.types import Block
from pylitmus.types import BlockHash
from pylitmus.types import BlockID
from pylitmus.types import EraID


def get_count(era_id: EraID = None) -> int:
    """Decaches a verified block.

    :param era_id: Era identifier.
    :returns: Verified block information.

    """
    with get_store(Partition.BLOCKS) as store:
        return store.get_count(
            ckey.count_of_self(era_id)
        )


def get(block_id: BlockID) -> bytes:
    """Decaches a verified block.

    :param block_id: Block identifier.
    :returns: Verified block information.

    """
    def _get_key():
        if isinstance(block_id, bytes):
            return ckey.from_hash(block_id)
        elif isinstance(block_id, int):
            return ckey.from_height(block_id)
        else:
            raise ValueError("Unrecognized block id")
    
    with get_store(Partition.BLOCKS) as store:
        return store.get_one_from_many(_get_key())


def get_by_parent_hash(block_hash: BlockHash) -> bytes:
    """Decaches a verified block by it's parent hash.

    :param block_id: Parent block hash.
    :returns: Verified block information.

    """
    with get_store(Partition.BLOCKS) as store:
        return store.get_one_from_many(
            ckey.from_parent_hash(block_hash)
        )


def get_by_era(era_id: EraID) -> bytes:
    """Decaches a verified block.

    :param era_id: Era identifier.
    :returns: Verified block information.

    """
    with get_store(Partition.BLOCKS) as store:
        return store.get_many(
            ckey.from_era(era_id)
        )


def get_switch(era_id: EraID) -> bytes:
    """Decaches a verified switch block.

    :param era_id: Era identifier.
    :returns: Verified switch block information.

    """
    with get_store(Partition.BLOCKS) as store:
        return store.get_many(
            ckey.from_era_at_switch(era_id)
        )


def set(entity: Block) -> str:
    """Encaches a verified block.

    :param entity: Block data to be cached.
    :returns: Cache key.

    """
    with get_store(Partition.BLOCKS) as store:
        return store.set_one_singleton(
            ckey.from_self(entity),
            json.dumps(pycspr.to_json(entity)),
        )
