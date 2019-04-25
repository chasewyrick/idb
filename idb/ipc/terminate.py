#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.


from idb.common.companion import CompanionClient
from idb.grpc.idb_pb2 import TerminateRequest


async def client(client: CompanionClient, bundle_id: str) -> None:
    await client.stub.terminate(TerminateRequest(bundle_id=bundle_id))
