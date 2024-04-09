import typing

from pycspr import crypto
from pycspr import serializer
from pycspr.types.cl import CLT_Type_ByteArray
from pycspr.types.cl import CLV_Bool
from pycspr.types.cl import CLV_ByteArray
from pycspr.types.cl import CLV_List
from pycspr.types.cl import CLV_Option
from pycspr.types.cl import CLV_PublicKey
from pycspr.types.cl import CLV_String
from pycspr.types.cl import CLV_U32
from pycspr.types.cl import CLV_U64
from pycspr.types.crypto import Digest
from pycspr.types.node.rpc import Block
from pycspr.types.node.rpc import BlockBody
from pycspr.types.node.rpc import BlockHeader
from pycspr.types.node.rpc import BlockHeight
from pycspr.types.node.rpc import BlockSignature
from pycspr.types.node.rpc import EraEnd
from pycspr.types.node.rpc import ProtocolVersion
from pycspr.utils.convertor import iso_datetime_from_timestamp


def get_digest_of_block(header: BlockHeader) -> Digest:
    # N.B. order matters !
    #
    #

    # CLV_Option(CLV_U64(correlation_id), CLT_Type_U64())

    return crypto.get_hash(
        serializer.to_bytes(
            CLV_ByteArray(header.parent_hash)
        ) +
        serializer.to_bytes(
            CLV_ByteArray(header.state_root)
        ) +
        serializer.to_bytes(
            CLV_ByteArray(header.body_hash)
        ) +
        serializer.to_bytes(
            CLV_Bool(header.random_bit)
        ) +
        serializer.to_bytes(
            CLV_ByteArray(header.accumulated_seed)
        ) +
        _encode_era_end(header.era_end) +
        serializer.to_bytes(
            CLV_U64(int(header.timestamp.value * 1000))
        ) +
        serializer.to_bytes(
            CLV_U64(header.era_id)
        ) +
        serializer.to_bytes(
            CLV_U64(header.height)
        ) +
        _encode_protocol_version(header.protocol_version)
    )


def _encode_era_end(entity: EraEnd) -> bytes:
    raise NotImplementedError()

    # serializer.to_bytes(
    #     CLV_Option(CLV_ByteArray(header.era_end), CLT_Type_ByteArray())
    # ) +


def _encode_protocol_version(entity: ProtocolVersion) -> bytes:
    return \
        serializer.to_bytes(CLV_U32(entity.major)) + \
        serializer.to_bytes(CLV_U32(entity.minor)) + \
        serializer.to_bytes(CLV_U32(entity.revision))


# let mut buffer = casper_types::bytesrepr::allocate_buffer(self)?;
# buffer.extend(self.parent_hash.to_bytes()?);
# buffer.extend(self.state_root_hash.to_bytes()?);
# buffer.extend(self.body_hash.to_bytes()?);
# buffer.extend(self.random_bit.to_bytes()?);
# buffer.extend(self.accumulated_seed.to_bytes()?);
# buffer.extend(self.era_end.to_bytes()?);
# buffer.extend(self.timestamp.to_bytes()?);
# buffer.extend(self.era_id.to_bytes()?);
# buffer.extend(self.height.to_bytes()?);
# buffer.extend(self.protocol_version.to_bytes()?);
# Ok(buffer)


# return crypto.get_hash(
#     serializer.to_bytes(
#         CLV_PublicKey.from_public_key(header.account_public_key)
#     ) +
#     serializer.to_bytes(
#         CLV_U64(int(header.timestamp.value * 1000))
#     ) +
#     serializer.to_bytes(
#         CLV_U64(header.ttl.as_milliseconds)
#     ) +
#     serializer.to_bytes(
#         CLV_U64(header.gas_price)
#     ) +
#     serializer.to_bytes(
#         CLV_ByteArray(header.body_hash)
#     ) +
#     serializer.to_bytes(
#         CLV_List(header.dependencies)
#     ) +
#     serializer.to_bytes(
#         CLV_String(header.chain_name)
#     )
# )
