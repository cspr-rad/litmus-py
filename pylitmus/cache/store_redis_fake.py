import fakeredis

from pylitmus.cache.model import StorePartition


def get_store(_: StorePartition) -> fakeredis.FakeStrictRedis:
    """Returns instance of a fake redis cache store accessor.

    :returns: An instance of a fake redis cache store accessor.

    """
    return fakeredis.FakeStrictRedis()
