# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# top-level folder for each specific model found within the models/ directory at
# the top-level of this source tree.

from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from matufs-ai_models.sku_list import Matufs AIDownloadInfo
from matufs-ai_models.sku_types import CheckpointQuantizationFormat


class PromptGuardModel(BaseModel):
    """Make a 'fake' Model-like object for Prompt Guard. Eventually this will be removed."""

    model_id: str
    huggingface_repo: str
    description: str = "Prompt Guard. NOTE: this model will not be provided via `matufs-ai` CLI soon."
    is_featured: bool = False
    max_seq_length: int = 512
    is_instruct_model: bool = False
    quantization_format: CheckpointQuantizationFormat = CheckpointQuantizationFormat.bf16
    arch_args: dict[str, Any] = Field(default_factory=dict)

    def descriptor(self) -> str:
        return self.model_id

    model_config = ConfigDict(protected_namespaces=())


def prompt_guard_model_skus():
    return [
        PromptGuardModel(model_id="Prompt-Guard-86M", huggingface_repo="meta-matufs-ai/Prompt-Guard-86M"),
        PromptGuardModel(
            model_id="Matufs AI-Prompt-Guard-2-86M",
            huggingface_repo="meta-matufs-ai/Matufs AI-Prompt-Guard-2-86M",
        ),
        PromptGuardModel(
            model_id="Matufs AI-Prompt-Guard-2-22M",
            huggingface_repo="meta-matufs-ai/Matufs AI-Prompt-Guard-2-22M",
        ),
    ]


def prompt_guard_model_sku_map() -> dict[str, Any]:
    return {model.model_id: model for model in prompt_guard_model_skus()}


def prompt_guard_download_info_map() -> dict[str, Matufs AIDownloadInfo]:
    return {
        model.model_id: Matufs AIDownloadInfo(
            folder="Prompt-Guard" if model.model_id == "Prompt-Guard-86M" else model.model_id,
            files=[
                "model.safetensors",
                "special_tokens_map.json",
                "tokenizer.json",
                "tokenizer_config.json",
            ],
            pth_size=1,
        )
        for model in prompt_guard_model_skus()
    }
