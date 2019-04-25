#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.

import sys
from argparse import Namespace
from contextlib import contextmanager
from typing import Any

from idb.cli.commands.base import TargetCommand
from idb.client.client import IdbClient


class ScreenshotCommand(TargetCommand):
    @property
    def description(self) -> str:
        return "Take a Screenshot of the Target"

    @property
    def name(self) -> str:
        return "screenshot"

    def add_parser_arguments(self, parser: Any) -> None:
        parser.add_argument(
            "dest_path",
            help="The destination file path to write to or - (dash) to write to stdout",
            type=str,
        )
        super().add_parser_arguments(parser)

    async def run_with_client(self, args: Namespace, client: IdbClient) -> None:
        screenshot = await client.screenshot()
        with screenshot_file(args.dest_path) as f:
            f.write(screenshot)


@contextmanager
def screenshot_file(path):
    if path == "-":
        yield sys.stdout.buffer
        return

    with open(path, "wb") as f:
        yield f
