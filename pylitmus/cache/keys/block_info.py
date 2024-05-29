from pylitmus.cache.keys.utils import get_key
from pylitmus.cache.model import Key
from pylitmus.types import BlockInfo


# Cache collection to which entity will be written.
_COLLECTION: str = "block-info"


def from_self(entity: BlockInfo) -> Key:
    return get_key(
        [
            _COLLECTION,
        ],
        [
            # Chain era.
            str(entity.era_id).zfill(12),
            # Block height.
            str(entity.height).zfill(12),
            # Block type.
            entity.typeof.value,
            # Block hash.
            entity.hash.hex(),
        ]
    )
