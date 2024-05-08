import redis

from pylitmus.cache.model import StorePartition
from pylitmus.utils import env



# Environment variables required by this module.
class EnvVars:
    # Redis host.
    DB: int = env.get_evar('CACHE_REDIS_DB', 1, int)

    # Redis host.
    HOST: str = env.get_evar('CACHE_REDIS_HOST', "localhost")

    # Redis port.
    PORT: int = env.get_evar('CACHE_REDIS_PORT', 6379, int)


# Map: partition type -> cache db index offset.
PARTITION_OFFSETS = {
    StorePartition.BLOCKS: 1,
    StorePartition.MERKLE_PROOFS: 2,
}


def get_store(partition_type: StorePartition) -> redis.Redis:
    """Returns instance of a redis cache store accessor.

    :returns: An instance of a redis cache store accessor.

    """
    # Set cache db index.
    db = EnvVars.DB
    db += PARTITION_OFFSETS[partition_type]

    # TODO: cluster connections
    return redis.Redis(
        db=db,
        host=EnvVars.HOST,
        port=EnvVars.PORT
        )