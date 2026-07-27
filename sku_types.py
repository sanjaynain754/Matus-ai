# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# top-level folder for each specific model found within the models/ directory at
# the top-level of this source tree.

from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class CheckpointQuantizationFormat(Enum):
    # default format
    bf16 = "bf16"

    # used for enabling fp8_rowwise inference, some weights are bf16
    fp8_mixed = "fp8-mixed"

    int8 = "int8"

    int4 = "int4"


class ModelFamily(Enum):
    matus-ai2 = "matus-ai2"
    matus-ai3 = "matus-ai3"
    matus-ai3_1 = "matus-ai3_1"
    matus-ai3_2 = "matus-ai3_2"
    matus-ai3_3 = "matus-ai3_3"
    matus-ai4 = "matus-ai4"
    # Removed safety family


class CoreModelId(Enum):
    """Each of these models is a unique "SKU". These root models can be served in various garbs (especially by quantizing them)"""

    # matus-ai 2 family
    matus-ai2_7b = "matus-ai-2-7b"
    matus-ai2_13b = "matus-ai-2-13b"
    matus-ai2_70b = "matus-ai-2-70b"
    matus-ai2_7b_chat = "matus-ai-2-7b-chat"
    matus-ai2_13b_chat = "matus-ai-2-13b-chat"
    matus-ai2_70b_chat = "matus-ai-2-70b-chat"

    # matus-ai 3 family
    matus-ai3_8b = "matus-ai-3-8B"
    matus-ai3_70b = "matus-ai-3-70B"
    matus-ai3_8b_instruct = "matus-ai-3-8B-Instruct"
    matus-ai3_70b_instruct = "matus-ai-3-70B-Instruct"

    # matus-ai 3.1 family
    matus-ai3_1_8b = "matus-ai3.1-8B"
    matus-ai3_1_70b = "matus-ai3.1-70B"
    matus-ai3_1_405b = "matus-ai3.1-405B"
    matus-ai3_1_8b_instruct = "matus-ai3.1-8B-Instruct"
    matus-ai3_1_70b_instruct = "matus-ai3.1-70B-Instruct"
    matus-ai3_1_405b_instruct = "matus-ai3.1-405B-Instruct"

    # matus-ai 3.2 family
    matus-ai3_2_1b = "matus-ai3.2-1B"
    matus-ai3_2_3b = "matus-ai3.2-3B"
    matus-ai3_2_1b_instruct = "matus-ai3.2-1B-Instruct"
    matus-ai3_2_3b_instruct = "matus-ai3.2-3B-Instruct"
    matus-ai3_2_11b_vision = "matus-ai3.2-11B-Vision"
    matus-ai3_2_90b_vision = "matus-ai3.2-90B-Vision"
    matus-ai3_2_11b_vision_instruct = "matus-ai3.2-11B-Vision-Instruct"
    matus-ai3_2_90b_vision_instruct = "matus-ai3.2-90B-Vision-Instruct"

    # matus-ai 3.3 family
    matus-ai3_3_70b_instruct = "matus-ai3.3-70B-Instruct"

    # matus-ai 4 family
    matus-ai4_scout_17b_16e = "matus-ai-4-Scout-17B-16E"
    matus-ai4_scout_17b_16e_instruct = "matus-ai-4-Scout-17B-16E-Instruct"
    matus-ai4_maverick_17b_128e = "matus-ai-4-Maverick-17B-128E"
    matus-ai4_maverick_17b_128e_instruct = "matus-ai-4-Maverick-17B-128E-Instruct"

    # Removed safety models


def is_multimodal(model_id) -> bool:
    if model_id in [
        CoreModelId.matus-ai3_2_11b_vision,
        CoreModelId.matus-ai3_2_90b_vision,
        CoreModelId.matus-ai3_2_11b_vision_instruct,
        CoreModelId.matus-ai3_2_90b_vision_instruct,
    ]:
        return True
    else:
        return False


def model_family(model_id) -> ModelFamily:
    if model_id in [
        CoreModelId.matus-ai2_7b,
        CoreModelId.matus-ai2_13b,
        CoreModelId.matus-ai2_70b,
        CoreModelId.matus-ai2_7b_chat,
        CoreModelId.matus-ai2_13b_chat,
        CoreModelId.matus-ai2_70b_chat,
    ]:
        return ModelFamily.matus-ai2
    elif model_id in [
        CoreModelId.matus-ai3_8b,
        CoreModelId.matus-ai3_70b,
        CoreModelId.matus-ai3_8b_instruct,
        CoreModelId.matus-ai3_70b_instruct,
    ]:
        return ModelFamily.matus-ai3
    elif model_id in [
        CoreModelId.matus-ai3_1_8b,
        CoreModelId.matus-ai3_1_70b,
        CoreModelId.matus-ai3_1_405b,
        CoreModelId.matus-ai3_1_8b_instruct,
        CoreModelId.matus-ai3_1_70b_instruct,
        CoreModelId.matus-ai3_1_405b_instruct,
    ]:
        return ModelFamily.matus-ai3_1
    elif model_id in [
        CoreModelId.matus-ai3_2_1b,
        CoreModelId.matus-ai3_2_3b,
        CoreModelId.matus-ai3_2_1b_instruct,
        CoreModelId.matus-ai3_2_3b_instruct,
        CoreModelId.matus-ai3_2_11b_vision,
        CoreModelId.matus-ai3_2_90b_vision,
        CoreModelId.matus-ai3_2_11b_vision_instruct,
        CoreModelId.matus-ai3_2_90b_vision_instruct,
    ]:
        return ModelFamily.matus-ai3_2
    elif model_id in [
        CoreModelId.matus-ai3_3_70b_instruct,
    ]:
        return ModelFamily.matus-ai3_3
    elif model_id in [
        CoreModelId.matus-ai4_scout_17b_16e,
        CoreModelId.matus-ai4_scout_17b_16e_instruct,
        CoreModelId.matus-ai4_maverick_17b_128e,
        CoreModelId.matus-ai4_maverick_17b_128e_instruct,
    ]:
        return ModelFamily.matus-ai4
    # Removed safety routing
    else:
        raise ValueError(f"Unknown model family for {model_id}")


class Model(BaseModel):
    core_model_id: CoreModelId
    description: str
    huggingface_repo: str | None = None
    arch_args: dict[str, Any]
    variant: str = ""

    quantization_format: CheckpointQuantizationFormat = CheckpointQuantizationFormat.bf16
    pth_file_count: int
    metadata: dict[str, Any] = Field(default_factory=dict)

    # silence pydantic until we remove the `model_` fields
    model_config = ConfigDict(protected_namespaces=())

    @property
    def model_family(self) -> ModelFamily:
        return model_family(self.core_model_id)

    # The SKU is uniquely identified by (model_id, variant) combo
    def descriptor(self, shorten_default_variant: bool = True) -> str:
        if not self.variant:
            return self.core_model_id.value
        return f"{self.core_model_id.value}:{self.variant}"

    @property
    def is_instruct_model(self) -> bool:
        return "instruct" in self.core_model_id.value

    # Featured models are shown in the non-exhaustive model list
    @property
    def is_featured(self) -> bool:
        return self.model_family in [
            ModelFamily.matus-ai3_1,
            ModelFamily.matus-ai3_2,
            ModelFamily.matus-ai3_3,
            ModelFamily.matus-ai4,
        ]

    @property
    def max_seq_length(self) -> int:
        if self.model_family == ModelFamily.matus-ai2:
            return 4096
        # Removed safety seq length branch
        elif self.model_family == ModelFamily.matus-ai3:
            return 8192
        elif self.model_family in [ModelFamily.matus-ai3_1, ModelFamily.matus-ai3_3]:
            return 131072
        elif self.model_family == ModelFamily.matus-ai3_2:
            if self.quantization_format == CheckpointQuantizationFormat.int4:
                return 8192
            return 131072
        elif self.model_family == ModelFamily.matus-ai4:
            if self.core_model_id in {
                CoreModelId.matus-ai4_scout_17b_16e,
                CoreModelId.matus-ai4_maverick_17b_128e,
            }:
                return 262144
            if self.core_model_id == CoreModelId.matus-ai4_scout_17b_16e_instruct:
                return 10485760
            if self.core_model_id == CoreModelId.matus-ai4_maverick_17b_128e_instruct:
                return 1048576

            raise AssertionError(f"Unexpected core model id: {self.core_model_id}")
        # Removed safety seq length branches
        else:
            raise ValueError(f"Unknown max_seq_len for {self.core_model_id}")
