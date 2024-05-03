import dataclasses
import typing

from pylitmus import chain

@dataclasses.dataclass
class BlockInfo():
    era: chain.EraID
    hash: chain.BlockHash
    height: chain.BlockHeight


_STORE_BY_ERA: dict = dict()
_STORE_BY_BLOCK: dict = dict()


async def init():
    # TODO: intiialise
    pass


def get_block_by_hash(block_hash: chain.BlockHash) -> typing.Optional[chain.Block]:
    try:
        return _STORE_BY_BLOCK[block_hash]
    except KeyError:
        pass


def get_block_by_height(block_height: chain.BlockHeight) -> typing.Optional[chain.Block]:
    try:
        return _STORE_BY_BLOCK[block_height]
    except KeyError:
        pass


def get_era_by_id(era_id: chain.EraID) -> typing.Optional[dict]:
    try:
        return _STORE_BY_ERA[era_id]
    except KeyError:
        pass


def set_verified_block(block: chain.Block):
    info: BlockInfo = BlockInfo(
        era = block.header.era_id,
        hash = block.hash,
        height = block.header.height,
    )

    if block.era_id not in _STORE_BY_ERA:
        _STORE_BY_ERA[block.era_id] = dict()
    if block.hash not in _STORE_BY_ERA[block.era_id]:
        _STORE_BY_ERA[block.era_id][block.hash] = info
    if block.height not in _STORE_BY_ERA[block.era_id]:
        _STORE_BY_ERA[block.era_id][block.height] = info

    if block.hash not in _STORE_BY_BLOCK:
        _STORE_BY_BLOCK[block.hash] = info
    if block.height not in _STORE_BY_BLOCK:
        _STORE_BY_BLOCK[block.height] = info
