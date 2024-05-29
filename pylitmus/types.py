import dataclasses
import enum
import typing

from pycspr.types.node import Block
from pycspr.types.node import BlockHash
from pycspr.types.node import BlockHeight
from pycspr.types.node import BlockID
from pycspr.types.node import EraID
from pycspr.types.node import ValidatorWeight
from pycspr.types.node import Weight


class BlockType(enum.Enum):
    """Types of block.
    
    """
    # Block produced during an era (excluding final round).
    STANDARD = 0

    # Block produced at final round of an era.
    SWITCH = 1


@dataclasses.dataclass
class BlockInfo():
    """Summary information over a verified block.
    
    """
    era_id: EraID
    hash: BlockHash
    height: BlockHeight
    typeof: BlockType

    @staticmethod
    def from_block(block: Block) -> "BlockInfo":
        return BlockInfo(
            era_id=block.header.era_id,
            hash=block.hash,
            height=block.header.height,
            typeof=BlockType.SWITCH if block.header.era_end else BlockType.STANDARD
        )

    def to_dict(self) -> dict:
        return {
            "era_id": self.era_id,
            "hash": self.hash.hex(),
            "height": self.height,
            "typeof": self.typeof.value,
        }


@dataclasses.dataclass
class EraConsensusWeights():
    """Summary information over a verified era.
    
    """
    era_id: EraID
    weights: typing.List[ValidatorWeight]

    @staticmethod
    def from_block(block: Block) -> "EraConsensusWeights":
        return EraConsensusWeights(
            era_id=block.header.era_id + 1,
            weights=block.header.era_end.next_era_validator_weights
        )

    def to_dict(self) -> dict:
        return {
            "era_id": self.era_id,
            "weights": [{
                "validator": i.validator.to_hex(),
                "weight": i.weight,
            } for i in self.weights]
        }
