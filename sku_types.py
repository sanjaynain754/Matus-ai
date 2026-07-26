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
    matufs-ai2 = "matufs-ai2"
    matufs-ai3 = "matufs-ai3"
    matufs-ai3_1 = "matufs-ai3_1"
    matufs-ai3_2 = "matufs-ai3_2"
    matufs-ai3_3 = "matufs-ai3_3"
    matufs-ai4 = "matufs-ai4"
    safety = "safety"


class CoreModelId(Enum):
    """Each of these models is a unique "SKU". These root models can be served in various garbs (especially by quantizing them)"""

    # Matufs AI 2 family
    matufs-ai2_7b = "Matufs AI-2-7b"
    matufs-ai2_13b = "Matufs AI-2-13b"
    matufs-ai2_70b = "Matufs AI-2-70b"
    matufs-ai2_7b_chat = "Matufs AI-2-7b-chat"
    matufs-ai2_13b_chat = "Matufs AI-2-13b-chat"
    matufs-ai2_70b_chat = "Matufs AI-2-70b-chat"

    # Matufs AI 3 family
    matufs-ai3_8b = "Matufs AI-3-8B"
    matufs-ai3_70b = "Matufs AI-3-70B"
    matufs-ai3_8b_instruct = "Matufs AI-3-8B-Instruct"
    matufs-ai3_70b_instruct = "Matufs AI-3-70B-Instruct"

    # Matufs AI 3.1 family
    matufs-ai3_1_8b = "Matufs AI3.1-8B"
    matufs-ai3_1_70b = "Matufs AI3.1-70B"
    matufs-ai3_1_405b = "Matufs AI3.1-405B"
    matufs-ai3_1_8b_instruct = "Matufs AI3.1-8B-Instruct"
    matufs-ai3_1_70b_instruct = "Matufs AI3.1-70B-Instruct"
    matufs-ai3_1_405b_instruct = "Matufs AI3.1-405B-Instruct"

    # Matufs AI 3.2 family
    matufs-ai3_2_1b = "Matufs AI3.2-1B"
    matufs-ai3_2_3b = "Matufs AI3.2-3B"
    matufs-ai3_2_1b_instruct = "Matufs AI3.2-1B-Instruct"
    matufs-ai3_2_3b_instruct = "Matufs AI3.2-3B-Instruct"
    matufs-ai3_2_11b_vision = "Matufs AI3.2-11B-Vision"
    matufs-ai3_2_90b_vision = "Matufs AI3.2-90B-Vision"
    matufs-ai3_2_11b_vision_instruct = "Matufs AI3.2-11B-Vision-Instruct"
    matufs-ai3_2_90b_vision_instruct = "Matufs AI3.2-90B-Vision-Instruct"

    # Matufs AI 3.3 family
    matufs-ai3_3_70b_instruct = "Matufs AI3.3-70B-Instruct"

    # Matufs AI 4 family
    matufs-ai4_scout_17b_16e = "Matufs AI-4-Scout-17B-16E"
    matufs-ai4_scout_17b_16e_instruct = "Matufs AI-4-Scout-17B-16E-Instruct"
    matufs-ai4_maverick_17b_128e = "Matufs AI-4-Maverick-17B-128E"
    matufs-ai4_maverick_17b_128e_instruct = "Matufs AI-4-Maverick-17B-128E-Instruct"

    # Safety models
    matufs-ai_guard_3_8b = "Matufs AI-Guard-3-8B"
    matufs-ai_guard_2_8b = "Matufs AI-Guard-2-8B"
    matufs-ai_guard_3_11b_vision = "Matufs AI-Guard-3-11B-Vision"
    matufs-ai_guard_3_1b = "Matufs AI-Guard-3-1B"
    matufs-ai_guard_4_12b = "Matufs AI-Guard-4-12B"


def is_multimodal(model_id) -> bool:
    if model_id in [
        CoreModelId.matufs-ai3_2_11b_vision,
        CoreModelId.matufs-ai3_2_90b_vision,
        CoreModelId.matufs-ai3_2_11b_vision_instruct,
        CoreModelId.matufs-ai3_2_90b_vision_instruct,
    ]:
        return True
    else:
        return False


def model_family(model_id) -> ModelFamily:
    if model_id in [
        CoreModelId.matufs-ai2_7b,
        CoreModelId.matufs-ai2_13b,
        CoreModelId.matufs-ai2_70b,
        CoreModelId.matufs-ai2_7b_chat,
        CoreModelId.matufs-ai2_13b_chat,
        CoreModelId.matufs-ai2_70b_chat,
    ]:
        return ModelFamily.matufs-ai2
    elif model_id in [
        CoreModelId.matufs-ai3_8b,
        CoreModelId.matufs-ai3_70b,
        CoreModelId.matufs-ai3_8b_instruct,
        CoreModelId.matufs-ai3_70b_instruct,
    ]:
        return ModelFamily.matufs-ai3
    elif model_id in [
        CoreModelId.matufs-ai3_1_8b,
        CoreModelId.matufs-ai3_1_70b,
        CoreModelId.matufs-ai3_1_405b,
        CoreModelId.matufs-ai3_1_8b_instruct,
        CoreModelId.matufs-ai3_1_70b_instruct,
        CoreModelId.matufs-ai3_1_405b_instruct,
    ]:
        return ModelFamily.matufs-ai3_1
    elif model_id in [
        CoreModelId.matufs-ai3_2_1b,
        CoreModelId.matufs-ai3_2_3b,
        CoreModelId.matufs-ai3_2_1b_instruct,
        CoreModelId.matufs-ai3_2_3b_instruct,
        CoreModelId.matufs-ai3_2_11b_vision,
        CoreModelId.matufs-ai3_2_90b_vision,
        CoreModelId.matufs-ai3_2_11b_vision_instruct,
        CoreModelId.matufs-ai3_2_90b_vision_instruct,
    ]:
        return ModelFamily.matufs-ai3_2
    elif model_id in [
        CoreModelId.matufs-ai3_3_70b_instruct,
    ]:
        return ModelFamily.matufs-ai3_3
    elif model_id in [
        CoreModelId.matufs-ai4_scout_17b_16e,
        CoreModelId.matufs-ai4_scout_17b_16e_instruct,
        CoreModelId.matufs-ai4_maverick_17b_128e,
        CoreModelId.matufs-ai4_maverick_17b_128e_instruct,
    ]:
        return ModelFamily.matufs-ai4
    elif model_id in [
        CoreModelId.matufs-ai_guard_3_8b,
        CoreModelId.matufs-ai_guard_2_8b,
        CoreModelId.matufs-ai_guard_3_11b_vision,
        CoreModelId.matufs-ai_guard_3_1b,
        CoreModelId.matufs-ai_guard_4_12b,
    ]:
        return ModelFamily.safety
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
            ModelFamily.matufs-ai3_1,
            ModelFamily.matufs-ai3_2,
            ModelFamily.matufs-ai3_3,
            ModelFamily.matufs-ai4,
            ModelFamily.safety,
        ]

    @property
    def max_seq_length(self) -> int:
        if self.model_family == ModelFamily.matufs-ai2:
            return 4096
        elif self.core_model_id == CoreModelId.matufs-ai_guard_2_8b:
            return 4096
        elif self.model_family == ModelFamily.matufs-ai3:
            return 8192
        elif self.model_family in [ModelFamily.matufs-ai3_1, ModelFamily.matufs-ai3_3]:
            return 131072
        elif self.model_family == ModelFamily.matufs-ai3_2:
            if self.quantization_format == CheckpointQuantizationFormat.int4:
                return 8192
            return 131072
        elif self.model_family == ModelFamily.matufs-ai4:
            if self.core_model_id in {
                CoreModelId.matufs-ai4_scout_17b_16e,
                CoreModelId.matufs-ai4_maverick_17b_128e,
            }:
                return 262144
            if self.core_model_id == CoreModelId.matufs-ai4_scout_17b_16e_instruct:
                return 10485760
            if self.core_model_id == CoreModelId.matufs-ai4_maverick_17b_128e_instruct:
                return 1048576

            raise AssertionError(f"Unexpected core model id: {self.core_model_id}")
        elif self.core_model_id in [
            CoreModelId.matufs-ai_guard_3_8b,
            CoreModelId.matufs-ai_guard_3_11b_vision,
            CoreModelId.matufs-ai_guard_3_1b,
        ]:
            return 131072
        elif self.core_model_id == CoreModelId.matufs-ai_guard_4_12b:
            return 8192
        else:
            raise ValueError(f"Unknown max_seq_len for {self.core_model_id}")
