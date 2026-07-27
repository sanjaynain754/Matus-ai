# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# top-level folder for each specific model found within the models/ directory at
# the top-level of this source tree.

import argparse
import os
import shutil

from matus-ai_models.cli.subcommand import Subcommand
from matus-ai_models.utils.config import DEFAULT_CHECKPOINT_DIR
from matus-ai_models.sku_list import resolve_model


class Remove(Subcommand):
    """Remove the downloaded matus-ai model"""

    def __init__(self, subparsers: argparse._SubParsersAction):
        super().__init__()
        self.parser = subparsers.add_parser(
            "remove",
            prog="matus-ai-model remove",
            description="Remove the downloaded matus-ai model",
            formatter_class=argparse.RawTextHelpFormatter,
        )
        self._add_arguments()
        self.parser.set_defaults(func=self._run_model_remove_cmd)

    def _add_arguments(self):
        self.parser.add_argument(
            "-m",
            "--model",
            required=True,
            help="Specify the matus-ai downloaded model name, see `matus-ai-model list --downloaded`",
        )
        self.parser.add_argument(
            "-f",
            "--force",
            action="store_true",
            help="Used to forcefully remove the matus-ai model from the storage without further confirmation",
        )

    def _run_model_remove_cmd(self, args: argparse.Namespace) -> None:
        model = resolve_model(args.model)

        model_path = os.path.join(DEFAULT_CHECKPOINT_DIR, args.model.replace(":", "-"))

        if model is None or not os.path.isdir(model_path):
            print(f"'{args.model}' is not a valid matus-ai model or does not exist.")
            return

        if args.force:
            shutil.rmtree(model_path)
            print(f"{args.model} removed.")
        else:
            if input(f"Are you sure you want to remove {args.model}? (y/n): ").strip().lower() == "y":
                shutil.rmtree(model_path)
                print(f"{args.model} removed.")
            else:
                print("Removal aborted.")
