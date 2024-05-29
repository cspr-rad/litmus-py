import time
import typing

from pylitmus.cache.model import Backend
from pylitmus.cache.model import Partition
from pylitmus.cache.stores.redis.client import get_client


# Max. number of times an operation will be tried.
_MAX_OP_ATTEMPTS: int = 5


class Proxy():
    """Proxy for interacting with a redis server.
    
    """
    def __init__(self, backend: Backend, partition: Partition):
        """Instance constructor.
        
        :params backend: Type if store backend to be utilised.
        :params partition: Store partition.
    
        """
        self.client = get_client(backend, partition)

    def __enter__(self):
        """Instance as context manager entry."""
        return self

    def __exit__(self, type, value, traceback):
        """Instance as context manager entry."""
        try:
            self.client.close()
        except:
            pass

    def decrement(self, ckey: str, count: int) -> int:
        """Decrements count under exactly matched key.

        :param ckey: Cache key.
        :param count: Decrementation delta.
        :returns: New counter value.
        
        """
        def _execute():
            return self.client.decrby(ckey, count)

        return _do_operation(_execute)

    def delete_one(self, ckey: str):
        """Deletes item under exactly matched key.
        
        """
        def _execute():
            self.client.delete(ckey)

        return _do_operation(_execute)

    def delete_many(self, ckey: str):
        """Deletes items under matching keys.

        """
        def _execute():
            chunk_size: int = 1000
            cursor: str = "0"
            while cursor != 0:
                cursor, keys = self.client.scan(cursor=cursor, match=ckey, count=chunk_size)
                if keys:
                    self.client.delete(*keys)

        return _do_operation(_execute)

    def get_count(self, ckey: str) -> int:
        """Returns length of collection under matched by key.
        
        :param ckey: Cache search key.
        :returns: Length of collection under matched by key.

        """
        def _execute():
            chunk_size: int = 1000
            count: int = 0
            cursor: str = "0"
            while cursor != 0:
                cursor, keys = self.client.scan(cursor=cursor, match=ckey, count=chunk_size)
                count += len(keys)
            return count

        return _do_operation(_execute)

    def get_one(self, ckey: str) -> bytes:
        """Returns cached entity matched by key.

        :param ckey: Cache key.
        :returns: Cached cached entity matched by key.
        
        """
        def _execute():
            return self.client.get(ckey)

        return _do_operation(_execute)

    def get_one_from_many(self, ckey: str) -> bytes:
        """Returns first cached entity matched by search key.

        :param ckey: Cache search key.
        :returns: Cached first cached entity matched by search key.
        
        """
        def _execute():
            chunk_size: int = 1000
            cursor: str = "0"
            while cursor != 0:
                cursor, keys = self.client.scan(cursor=cursor, match=ckey, count=chunk_size)   
                if keys:
                    return self.client.get(keys[0])
                
        return _do_operation(_execute)

    def get_many(self, ckey: str) -> typing.List[bytes]:
        """Returns cached entities matched by search key.

        :param ckey: Cache search key.
        :returns: Cached entities matched by search key.
        
        """
        def _execute():
            chunk_size: int = 2000
            cursor: str = "0"
            keys: typing.List[str] = []
            while cursor != 0:
                cursor, keys_ = self.client.scan(cursor=cursor, match=ckey, count=chunk_size)
                keys += keys_
            return self.client.mget(keys)

        return _do_operation(_execute)

    def increment(self, ckey: str, count: int) -> int:
        """Increments count under exactly matched key.

        :param ckey: Cache key.
        :param count: Incrementation delta.
        :returns: New counter value.
        
        """
        def _execute():
            return self.client.incrby(ckey, count)
        
        return _do_operation(_execute)

    def set_one(self, ckey: str, cdata: typing.Any, cexpiration: int = None):
        """Sets entity under a key.

        :param ckey: Cache key.
        :param cdata: Date to be encached.
        :param cexpiration: Cache key expiration in milliseconds.
        
        """
        def _execute():
            self.client.set(ckey, cdata, ex=cexpiration)
        
        return _do_operation(_execute)

    def set_one_singleton(
        self,
        ckey: str,
        cdata: typing.Any,
        cexpiration: int = None
    ) -> bool:
        """Sets entity under a key if not already cached.

        :param ckey: Cache key.
        :param cdata: Date to be encached.
        :param cexpiration: Cache key expiration in milliseconds.
        :returns: Flag indicating whether caching operation occurred.
        
        """
        def _execute():
            was_cached: bool = bool(self.client.setnx(ckey, cdata))
            if was_cached and cexpiration:
                self.client.expire(ckey, cexpiration)
            return was_cached  

        return _do_operation(_execute)


def _do_operation(operation):
    """Executes a cache operation."""
    attempts: int = 0
    while attempts < _MAX_OP_ATTEMPTS:
        time.sleep(0.01)
        try:
            return operation()
        except BaseException as err:
            attempts += 1
            if attempts == _MAX_OP_ATTEMPTS:
                raise err
            time.sleep(0.01)


# def cache_op(partition: StorePartition, operation: StoreOperation) -> typing.Callable:
#     """Decorator to orthoganally process a cache operation.

#     :param partition: Cache partition to which operation pertains.
#     :param operation: Cache operation to apply.

#     :returns: Decorated function.
    
#     """
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             with stores.get_store(partition) as store:
#                 # Invoke inner function.
#                 obj = func(*args, **kwargs)
#                 if obj is None:
#                     return

#                 # Invoke operation applying retry semantics in case of broken pipes.
#                 attempts = 0
#                 handler = _HANDLERS[operation]
#                 while attempts < _MAX_OP_ATTEMPTS:
#                     try:
#                         return handler(store, obj)
#                     except redis.ConnectionError as err:
#                         attempts += 1
#                         if attempts == _MAX_OP_ATTEMPTS:
#                             raise err
#                         time.sleep(float(0.01))

#         return wrapper
#     return decorator
