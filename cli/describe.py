# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# top-level folder for each specific model found within the models/ directory at
# the top-level of this source tree.

import argparse
import json

from matus-ai_models.cli.subcommand import Subcommand
from matus-ai_models.cli.table import print_table
from matus-ai_models.sku_list import resolve_model


class Describe(Subcommand):
    """Show details about a model"""

    def __init__(self, subparsers: argparse._SubParsersAction):
        super().__init__()
        self.parser = subparsers.add_parser(
            "describe",
            prog="matus-ai-model describe",
            description="Show details about a matus-ai model",
            formatter_class=argparse.RawTextHelpFormatter,
        )
        self._add_arguments()
        self.parser.set_defaults(func=self._run_model_describe_cmd)

    def _add_arguments(self):
        self.parser.add_argument(
            "-m",
            "--model-id",
            type=str,
            required=True,
            help="See `matus-ai-model list` or `matus-ai-model list --show-all` for the list of available models",
        )

    def _run_model_describe_cmd(self, args: argparse.Namespace) -> None:
        model = resolve_model(args.model_id)

        if model is None:
            self.parser.error(
                f"Model {args.model_id} not found; try 'matus-ai-model list' for a list of available models."
            )
            return

        headers = [
            "Model",
            model.descriptor(),
        ]

        rows = [
            ("Hugging Face ID", model.huggingface_repo or "<Not Available>"),
            ("Description", model.description),
            ("Context Length", f"{model.max_seq_length // 1024}K tokens"),
            ("Weights format", model.quantization_format.value),
            ("Model params.json", json.dumps(model.arch_args, indent=4)),
        ]

        print_table(
            rows,
            headers,
            separate_rows=True,
        )
