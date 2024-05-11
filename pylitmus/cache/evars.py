from pylitmus.cache.model import Backend
from pylitmus.utils import env


# Cache backend.
BACKEND: Backend = Backend[env.get_evar("CACHE", Backend.REDIS.value)]

# Redis backend :: db index.
REDIS_DB: int = env.get_evar('CACHE_REDIS_DB', 1, int)

# Redis backend :: host.
REDIS_HOST: str = env.get_evar('CACHE_REDIS_HOST', "localhost")

# Redis backend :: port.
REDIS_PORT: int = env.get_evar('CACHE_REDIS_PORT', 6379, int)
