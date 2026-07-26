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
    matuss-ai2 = "matuss-ai2"
    matuss-ai3 = "matuss-ai3"
    matuss-ai3_1 = "matuss-ai3_1"
    matuss-ai3_2 = "matuss-ai3_2"
    matuss-ai3_3 = "matuss-ai3_3"
    matuss-ai4 = "matuss-ai4"
    safety = "safety"


class CoreModelId(Enum):
    """Each of these models is a unique "SKU". These root models can be served in various garbs (especially by quantizing them)"""

    # Matuss AI 2 family
    matuss-ai2_7b = "Matuss AI-2-7b"
    matuss-ai2_13b = "Matuss AI-2-13b"
    matuss-ai2_70b = "Matuss AI-2-70b"
    matuss-ai2_7b_chat = "Matuss AI-2-7b-chat"
    matuss-ai2_13b_chat = "Matuss AI-2-13b-chat"
    matuss-ai2_70b_chat = "Matuss AI-2-70b-chat"

    # Matuss AI 3 family
    matuss-ai3_8b = "Matuss AI-3-8B"
    matuss-ai3_70b = "Matuss AI-3-70B"
    matuss-ai3_8b_instruct = "Matuss AI-3-8B-Instruct"
    matuss-ai3_70b_instruct = "Matuss AI-3-70B-Instruct"

    # Matuss AI 3.1 family
    matuss-ai3_1_8b = "Matuss AI3.1-8B"
    matuss-ai3_1_70b = "Matuss AI3.1-70B"
    matuss-ai3_1_405b = "Matuss AI3.1-405B"
    matuss-ai3_1_8b_instruct = "Matuss AI3.1-8B-Instruct"
    matuss-ai3_1_70b_instruct = "Matuss AI3.1-70B-Instruct"
    matuss-ai3_1_405b_instruct = "Matuss AI3.1-405B-Instruct"

    # Matuss AI 3.2 family
    matuss-ai3_2_1b = "Matuss AI3.2-1B"
    matuss-ai3_2_3b = "Matuss AI3.2-3B"
    matuss-ai3_2_1b_instruct = "Matuss AI3.2-1B-Instruct"
    matuss-ai3_2_3b_instruct = "Matuss AI3.2-3B-Instruct"
    matuss-ai3_2_11b_vision = "Matuss AI3.2-11B-Vision"
    matuss-ai3_2_90b_vision = "Matuss AI3.2-90B-Vision"
    matuss-ai3_2_11b_vision_instruct = "Matuss AI3.2-11B-Vision-Instruct"
    matuss-ai3_2_90b_vision_instruct = "Matuss AI3.2-90B-Vision-Instruct"

    # Matuss AI 3.3 family
    matuss-ai3_3_70b_instruct = "Matuss AI3.3-70B-Instruct"

    # Matuss AI 4 family
    matuss-ai4_scout_17b_16e = "Matuss AI-4-Scout-17B-16E"
    matuss-ai4_scout_17b_16e_instruct = "Matuss AI-4-Scout-17B-16E-Instruct"
    matuss-ai4_maverick_17b_128e = "Matuss AI-4-Maverick-17B-128E"
    matuss-ai4_maverick_17b_128e_instruct = "Matuss AI-4-Maverick-17B-128E-Instruct"

    # Safety models
    matuss-ai_guard_3_8b = "Matuss AI-Guard-3-8B"
    matuss-ai_guard_2_8b = "Matuss AI-Guard-2-8B"
    matuss-ai_guard_3_11b_vision = "Matuss AI-Guard-3-11B-Vision"
    matuss-ai_guard_3_1b = "Matuss AI-Guard-3-1B"
    matuss-ai_guard_4_12b = "Matuss AI-Guard-4-12B"


def is_multimodal(model_id) -> bool:
    if model_id in [
        CoreModelId.matuss-ai3_2_11b_vision,
        CoreModelId.matuss-ai3_2_90b_vision,
        CoreModelId.matuss-ai3_2_11b_vision_instruct,
        CoreModelId.matuss-ai3_2_90b_vision_instruct,
    ]:
        return True
    else:
        return False


def model_family(model_id) -> ModelFamily:
    if model_id in [
        CoreModelId.matuss-ai2_7b,
        CoreModelId.matuss-ai2_13b,
        CoreModelId.matuss-ai2_70b,
        CoreModelId.matuss-ai2_7b_chat,
        CoreModelId.matuss-ai2_13b_chat,
        CoreModelId.matuss-ai2_70b_chat,
    ]:
        return ModelFamily.matuss-ai2
    elif model_id in [
        CoreModelId.matuss-ai3_8b,
        CoreModelId.matuss-ai3_70b,
        CoreModelId.matuss-ai3_8b_instruct,
        CoreModelId.matuss-ai3_70b_instruct,
    ]:
        return ModelFamily.matuss-ai3
    elif model_id in [
        CoreModelId.matuss-ai3_1_8b,
        CoreModelId.matuss-ai3_1_70b,
        CoreModelId.matuss-ai3_1_405b,
        CoreModelId.matuss-ai3_1_8b_instruct,
        CoreModelId.matuss-ai3_1_70b_instruct,
        CoreModelId.matuss-ai3_1_405b_instruct,
    ]:
        return ModelFamily.matuss-ai3_1
    elif model_id in [
        CoreModelId.matuss-ai3_2_1b,
        CoreModelId.matuss-ai3_2_3b,
        CoreModelId.matuss-ai3_2_1b_instruct,
        CoreModelId.matuss-ai3_2_3b_instruct,
        CoreModelId.matuss-ai3_2_11b_vision,
        CoreModelId.matuss-ai3_2_90b_vision,
        CoreModelId.matuss-ai3_2_11b_vision_instruct,
        CoreModelId.matuss-ai3_2_90b_vision_instruct,
    ]:
        return ModelFamily.matuss-ai3_2
    elif model_id in [
        CoreModelId.matuss-ai3_3_70b_instruct,
    ]:
        return ModelFamily.matuss-ai3_3
    elif model_id in [
        CoreModelId.matuss-ai4_scout_17b_16e,
        CoreModelId.matuss-ai4_scout_17b_16e_instruct,
        CoreModelId.matuss-ai4_maverick_17b_128e,
        CoreModelId.matuss-ai4_maverick_17b_128e_instruct,
    ]:
        return ModelFamily.matuss-ai4
    elif model_id in [
        CoreModelId.matuss-ai_guard_3_8b,
        CoreModelId.matuss-ai_guard_2_8b,
        CoreModelId.matuss-ai_guard_3_11b_vision,
        CoreModelId.matuss-ai_guard_3_1b,
        CoreModelId.matuss-ai_guard_4_12b,
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
            ModelFamily.matuss-ai3_1,
            ModelFamily.matuss-ai3_2,
            ModelFamily.matuss-ai3_3,
            ModelFamily.matuss-ai4,
            ModelFamily.safety,
        ]

    @property
    def max_seq_length(self) -> int:
        if self.model_family == ModelFamily.matuss-ai2:
            return 4096
        elif self.core_model_id == CoreModelId.matuss-ai_guard_2_8b:
            return 4096
        elif self.model_family == ModelFamily.matuss-ai3:
            return 8192
        elif self.model_family in [ModelFamily.matuss-ai3_1, ModelFamily.matuss-ai3_3]:
            return 131072
        elif self.model_family == ModelFamily.matuss-ai3_2:
            if self.quantization_format == CheckpointQuantizationFormat.int4:
                return 8192
            return 131072
        elif self.model_family == ModelFamily.matuss-ai4:
            if self.core_model_id in {
                CoreModelId.matuss-ai4_scout_17b_16e,
                CoreModelId.matuss-ai4_maverick_17b_128e,
            }:
                return 262144
            if self.core_model_id == CoreModelId.matuss-ai4_scout_17b_16e_instruct:
                return 10485760
            if self.core_model_id == CoreModelId.matuss-ai4_maverick_17b_128e_instruct:
                return 1048576

            raise AssertionError(f"Unexpected core model id: {self.core_model_id}")
        elif self.core_model_id in [
            CoreModelId.matuss-ai_guard_3_8b,
            CoreModelId.matuss-ai_guard_3_11b_vision,
            CoreModelId.matuss-ai_guard_3_1b,
        ]:
            return 131072
        elif self.core_model_id == CoreModelId.matuss-ai_guard_4_12b:
            return 8192
        else:
            raise ValueError(f"Unknown max_seq_len for {self.core_model_id}")
