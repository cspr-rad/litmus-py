import dataclasses
import enum
import typing

from pycspr.types.node.rpc import BlockHash
from pycspr.types.node.rpc import EraEnd


@dataclasses.dataclass
class Kernel:
    block_hash: BlockHash
    block_hash_of_parent: typing.Optional[BlockHash] = None
    block_height: typing.Optional[int] = None
    era_end: typing.Optional[EraEnd] = None


class KernelError(enum.Enum):
    INVALID_BLOCK_HASH_UPON_INITIALIZATION = enum.auto()
    INVALID_BLOCK_HASH_UPON_REVERSE_SYNC = enum.auto()
    HISTORICAL_BLOCK_WHEN_PROGRESSING = enum.auto()
    INVALID_ERA_ID = enum.auto()
    INVALID_BLCK_SIGNATURES = enum.auto()


@dataclasses.dataclass
class KernelState:
    kernel: Kernel
