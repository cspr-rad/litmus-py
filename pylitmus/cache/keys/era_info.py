from pylitmus.cache.keys.utils import get_key
from pylitmus.cache.model import Key
from pylitmus.types import EraConsensusWeights


# Cache collection to which entity will be written.
_COLLECTION: str = "era-info"


def from_self(entity: EraConsensusWeights) -> Key:
    return get_key(
        [
            _COLLECTION,
        ],
        [
            # Chain era.
            str(entity.era_id).zfill(12),
        ]
    )
