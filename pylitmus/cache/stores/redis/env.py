from pylitmus.utils import env


# Redis host.
REDIS_DB: int = env.get_evar('CACHE_REDIS_DB', 1, int)

# Redis host.
REDIS_HOST: str = env.get_evar('CACHE_REDIS_HOST', "localhost")

# Redis port.
REDIS_PORT: int = env.get_evar('CACHE_REDIS_PORT', 6379, int)
