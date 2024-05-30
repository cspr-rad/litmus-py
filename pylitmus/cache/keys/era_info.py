from pylitmus.cache.keys.utils import get_key
from pylitmus.cache.model import Key
from pylitmus.types import EraInfo


# Cache collection to which entity will be written.
_COLLECTION: str = "era-info"


def from_id(era_id: int) -> Key:
    return get_key(
        [
            _COLLECTION,
        ],
        [
            # Chain era.
            str(era_id).zfill(12),
        ]
    )


def from_self(entity: EraInfo) -> Key:
    return get_key(
        [
            _COLLECTION,
        ],
        [
            # Chain era.
            str(entity.era_id).zfill(12),
        ]
    )
