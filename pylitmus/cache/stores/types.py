import enum

from pylitmus.utils import env


class Backend(enum.Enum):
    """Enumeration over set of supported backends.
    
    """
    REDIS = "REDIS"
    REDIS_FAKE = "REDIS_FAKE"


# User defined backend type - from environment.
BACKEND: Backend = Backend[env.get_evar("CACHE", Backend.REDIS.value)]
