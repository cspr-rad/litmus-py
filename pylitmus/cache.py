import json
import os
import pathlib
import sys
import typing

from pycspr import NodeRpcClient

from pylitmus import chain



_STORE_BY_HASH: dict = dict()
_STORE_BY_HEIGHT: dict = dict()

import pycspr
from pycspr.types.node.rpc import Block


def init():
    # TODO: intiialise
    pass


def get_block_by_hash(block_hash: chain.BlockHash) -> typing.Optional[Block]:
    try:
        return _STORE_BY_HASH[block_hash]
    except KeyError:
        pass


def get_block_by_height(block_height: chain.BlockHeight) -> typing.Optional[Block]:
    try:
        return _STORE_BY_HEIGHT[block_height]
    except KeyError:
        pass


def set_block(block: chain.Block):
    if block.hash not in _STORE_BY_HASH:
        _STORE_BY_HASH[block.hash] = block
    if block.height not in _STORE_BY_HEIGHT:
        _STORE_BY_HEIGHT[block.height] = block
