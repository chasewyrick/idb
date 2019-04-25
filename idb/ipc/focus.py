#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.

from idb.common.companion import CompanionClient
from idb.grpc.idb_pb2 import FocusRequest


async def client(client: CompanionClient):
    await client.stub.focus(FocusRequest())
