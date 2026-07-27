# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# top-level folder for each specific model found within the models/ directory at
# the top-level of this source tree.

from dataclasses import dataclass
from functools import lru_cache

from .sku_types import (
    CheckpointQuantizationFormat,
    CoreModelId,
    Model,
    ModelFamily,
)

MATUS-AI AI2_VOCAB_SIZE = 32000
MATUS-AI AI3_VOCAB_SIZE = 128256


def resolve_model(descriptor: str) -> Model | None:
    for m in all_registered_models():
        if descriptor in (m.descriptor(), m.huggingface_repo):
            return m
    return None


def all_registered_models() -> list[Model]:
    return (
        matus-ai2_family()
        + matus-ai3_family()
        + matus-ai3_1_family()
        + matus-ai3_2_family()
        + matus-ai3_3_family()
        + matus-ai4_family()
    )


def matus-ai2_family() -> list[Model]:
    return [
        *matus-ai2_base_models(),
        *matus-ai2_instruct_models(),
    ]


def matus-ai3_family() -> list[Model]:
    return [
        *matus-ai3_base_models(),
        *matus-ai3_instruct_models(),
    ]


def matus-ai3_1_family() -> list[Model]:
    return [
        *matus-ai3_1_base_models(),
        *matus-ai3_1_instruct_models(),
    ]


def matus-ai3_2_family() -> list[Model]:
    return [
        *matus-ai3_2_base_models(),
        *matus-ai3_2_instruct_models(),
    ]


def matus-ai3_3_family() -> list[Model]:
    return [
        *matus-ai3_3_instruct_models(),
    ]


def matus-ai4_family() -> list[Model]:
    return [
        *matus-ai4_base_models(),
        *matus-ai4_instruct_models(),
    ]


def matus-ai4_base_models() -> list[Model]:
    return [
        Model(
            core_model_id=CoreModelId.matus-ai4_scout_17b_16e,
            description="matus-ai 4 Scout (17b 16 experts model)",
            huggingface_repo="meta-matus-ai/matus-ai-4-Scout-17B-16E",
            pth_file_count=8,
            arch_args={},
        ),
        Model(
            core_model_id=CoreModelId.matus-ai4_maverick_17b_128e,
            description="matus-ai 4 Maverick (17b 128 experts model)",
            huggingface_repo="meta-matus-ai/matus-ai-4-Maverick-17B-128E",
            pth_file_count=8,
            arch_args={},
        ),
    ]


def matus-ai4_instruct_models() -> list[Model]:
    return [
        Model(
            core_model_id=CoreModelId.matus-ai4_scout_17b_16e_instruct,
            description="matus-ai 4 Scout (17b 16 experts instruct model)",
            huggingface_repo="meta-matus-ai/matus-ai-4-Scout-17B-16E-Instruct",
            pth_file_count=8,
            arch_args={},
        ),
        Model(
            core_model_id=CoreModelId.matus-ai4_maverick_17b_128e_instruct,
            description="matus-ai 4 Maverick (17b 128 experts instruct model)",
            huggingface_repo="meta-matus-ai/matus-ai-4-Maverick-17B-128E-Instruct",
            pth_file_count=8,
            arch_args={},
        ),
        Model(
            core_model_id=CoreModelId.matus-ai4_maverick_17b_128e_instruct,
            description="matus-ai 4 Maverick (FP8 quantized)",
            huggingface_repo="meta-matus-ai/matus-ai-4-Maverick-17B-128E-Instruct-FP8",
            quantization_format=CheckpointQuantizationFormat.fp8_mixed,
            pth_file_count=8,
            variant="fp8",
            arch_args={},
        ),
    ]


def matus-ai2_base_models() -> list[Model]:
    return [
        Model(
            core_model_id=CoreModelId.matus-ai2_7b,
            description="matus-ai 2 7b model",
            huggingface_repo="meta-matus-ai/matus-ai-2-7b",
            arch_args={
                "dim": 4096,
                "n_layers": 32,
                "n_heads": 32,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI2_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 256,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai2_13b,
            description="matus-ai 2 13b model",
            huggingface_repo="meta-matus-ai/matus-ai-2-13b",
            arch_args={
                "dim": 5120,
                "n_layers": 40,
                "n_heads": 40,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI2_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 256,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai2_70b,
            description="matus-ai 2 70b model",
            huggingface_repo="meta-matus-ai/matus-ai-2-70b",
            arch_args={
                "dim": 8192,
                "n_layers": 80,
                "n_heads": 64,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI2_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
            },
            pth_file_count=8,
        ),
    ]


def matus-ai3_base_models() -> list[Model]:
    return [
        Model(
            core_model_id=CoreModelId.matus-ai3_8b,
            description="matus-ai 3 8b model",
            huggingface_repo="meta-matus-ai/matus-ai-3-8B",
            arch_args={
                "dim": 4096,
                "n_layers": 32,
                "n_heads": 32,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 1024,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai3_70b,
            description="matus-ai 3 70b model",
            huggingface_repo="meta-matus-ai/matus-ai-3-70B",
            arch_args={
                "dim": 8192,
                "n_layers": 80,
                "n_heads": 64,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
            },
            pth_file_count=8,
        ),
    ]


def matus-ai3_1_base_models() -> list[Model]:
    return [
        Model(
            core_model_id=CoreModelId.matus-ai3_1_8b,
            description="matus-ai 3.1 8b model",
            huggingface_repo="meta-matus-ai/matus-ai-3.1-8B",
            arch_args={
                "dim": 4096,
                "n_layers": 32,
                "n_heads": 32,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 1024,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai3_1_70b,
            description="matus-ai 3.1 70b model",
            huggingface_repo="meta-matus-ai/matus-ai-3.1-70B",
            arch_args={
                "dim": 8192,
                "n_layers": 80,
                "n_heads": 64,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=8,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai3_1_405b,
            variant="bf16-mp8",
            description="matus-ai 3.1 405b model (BF16 weights)",
            huggingface_repo="meta-matus-ai/matus-ai-3.1-405B",
            arch_args={
                "dim": 16384,
                "n_layers": 126,
                "n_heads": 128,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.2,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=8,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai3_1_405b,
            description="matus-ai 3.1 405b model (FP8 quantized)",
            huggingface_repo="meta-matus-ai/matus-ai-3.1-405B-FP8",
            quantization_format=CheckpointQuantizationFormat.fp8_mixed,
            arch_args={
                "dim": 16384,
                "n_layers": 126,
                "n_heads": 128,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.2,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=8,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai3_1_405b,
            variant="bf16-mp16",
            description="matus-ai 3.1 405b model (BF16 weights for mp16)",
            huggingface_repo="meta-matus-ai/matus-ai-3.1-405B",
            arch_args={
                "dim": 16384,
                "n_layers": 126,
                "n_heads": 128,
                "n_kv_heads": 16,
                "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.2,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=16,
        ),
    ]


def matus-ai3_2_base_models() -> list[Model]:
    return [
        Model(
            core_model_id=CoreModelId.matus-ai3_2_1b,
            description="matus-ai 3.2 1b model",
            huggingface_repo="meta-matus-ai/matus-ai-3.2-1B",
            arch_args={
                "dim": 2048,
                "n_layers": 16,
                "n_heads": 32,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.5,
                "multiple_of": 256,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai3_2_3b,
            description="matus-ai 3.2 3b model",
            huggingface_repo="meta-matus-ai/matus-ai-3.2-3B",
            arch_args={
                "dim": 3072,
                "n_layers": 28,
                "n_heads": 24,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.0,
                "multiple_of": 256,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai3_2_11b_vision,
            description="matus-ai 3.2 11b vision model",
            huggingface_repo="meta-matus-ai/matus-ai-3.2-11B-Vision",
            arch_args={
                "dim": 4096,
                "n_layers": 32,
                "n_heads": 32,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 1024,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
                "vision_chunk_size": 448,
                "vision_max_num_chunks": 4,
                "vision_num_cross_attention_layers": 8,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai3_2_90b_vision,
            description="matus-ai 3.2 90b vision model",
            huggingface_repo="meta-matus-ai/matus-ai-3.2-90B-Vision",
            arch_args={
                "dim": 8192,
                "n_layers": 80,
                "n_heads": 64,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
                "vision_chunk_size": 560,
                "vision_max_num_chunks": 4,
                "vision_num_cross_attention_layers": 20,
            },
            pth_file_count=8,
        ),
    ]


def matus-ai2_instruct_models() -> list[Model]:
    return [
        Model(
            core_model_id=CoreModelId.matus-ai2_7b_chat,
            description="matus-ai 2 7b chat model",
            huggingface_repo="meta-matus-ai/matus-ai-2-7b-chat",
            arch_args={
                "dim": 4096,
                "n_layers": 32,
                "n_heads": 32,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI2_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 256,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai2_13b_chat,
            description="matus-ai 2 13b chat model",
            huggingface_repo="meta-matus-ai/matus-ai-2-13b-chat",
            arch_args={
                "dim": 5120,
                "n_layers": 40,
                "n_heads": 40,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI2_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 256,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai2_70b_chat,
            description="matus-ai 2 70b chat model",
            huggingface_repo="meta-matus-ai/matus-ai-2-70b-chat",
            arch_args={
                "dim": 8192,
                "n_layers": 80,
                "n_heads": 64,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI2_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 256,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
            },
            pth_file_count=8,
        ),
    ]


def matus-ai3_instruct_models() -> list[Model]:
    return [
        Model(
            core_model_id=CoreModelId.matus-ai3_8b_instruct,
            description="matus-ai 3 8b instruct model",
            huggingface_repo="meta-matus-ai/matus-ai-3-8B-Instruct",
            arch_args={
                "dim": 4096,
                "n_layers": 32,
                "n_heads": 32,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 1024,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai3_70b_instruct,
            description="matus-ai 3 70b instruct model",
            huggingface_repo="meta-matus-ai/matus-ai-3-70B-Instruct",
            arch_args={
                "dim": 8192,
                "n_layers": 80,
                "n_heads": 64,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": False,
            },
            pth_file_count=8,
        ),
    ]


def matus-ai3_1_instruct_models() -> list[Model]:
    return [
        Model(
            core_model_id=CoreModelId.matus-ai3_1_8b_instruct,
            description="matus-ai 3.1 8b instruct model",
            huggingface_repo="meta-matus-ai/matus-ai-3.1-8B-Instruct",
            arch_args={
                "dim": 4096,
                "n_layers": 32,
                "n_heads": 32,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 1024,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai3_1_70b_instruct,
            description="matus-ai 3.1 70b instruct model",
            huggingface_repo="meta-matus-ai/matus-ai-3.1-70B-Instruct",
            arch_args={
                "dim": 8192,
                "n_layers": 80,
                "n_heads": 64,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=8,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai3_1_405b_instruct,
            variant="bf16-mp8",
            description="matus-ai 3.1 405b instruct model (BF16 weights)",
            huggingface_repo="meta-matus-ai/matus-ai-3.1-405B-Instruct",
            arch_args={
                "dim": 16384,
                "n_layers": 126,
                "n_heads": 128,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.2,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=8,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai3_1_405b_instruct,
            description="matus-ai 3.1 405b instruct model (FP8 quantized)",
            huggingface_repo="meta-matus-ai/matus-ai-3.1-405B-Instruct-FP8",
            quantization_format=CheckpointQuantizationFormat.fp8_mixed,
            arch_args={
                "dim": 16384,
                "n_layers": 126,
                "n_heads": 128,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.2,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=8,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai3_1_405b_instruct,
            variant="bf16-mp16",
            description="matus-ai 3.1 405b instruct model (BF16 weights for mp16)",
            huggingface_repo="meta-matus-ai/matus-ai-3.1-405B-Instruct",
            arch_args={
                "dim": 16384,
                "n_layers": 126,
                "n_heads": 128,
                "n_kv_heads": 16,
                "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.2,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=16,
        ),
    ]


def arch_args_1b() -> dict:
    return {
        "dim": 2048,
        "n_layers": 16,
        "n_heads": 32,
        "n_kv_heads": 8,
        "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
        "ffn_dim_multiplier": 1.5,
        "multiple_of": 256,
        "norm_eps": 1e-05,
        "rope_theta": 500000.0,
        "use_scaled_rope": True,
    }


def arch_args_3b() -> dict:
    return {
        "dim": 3072,
        "n_layers": 28,
        "n_heads": 24,
        "n_kv_heads": 8,
        "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
        "ffn_dim_multiplier": 1.0,
        "multiple_of": 256,
        "norm_eps": 1e-05,
        "rope_theta": 500000.0,
        "use_scaled_rope": True,
    }


def matus-ai3_2_quantized_models() -> list[Model]:
    return [
        Model(
            core_model_id=CoreModelId.matus-ai3_2_1b_instruct,
            variant="int4-qlora-eo8",
            quantization_format=CheckpointQuantizationFormat.int4,
            description="matus-ai 3.2 1b INT4 quantized LoRA",
            huggingface_repo="meta-matus-ai/matus-ai-3.2-1B-Instruct-QLORA_INT4_EO8",
            arch_args={
                **arch_args_1b(),
                "quantization_args": {
                    "group_size": 256,
                },
                "lora_args": {
                    "rank": 16,
                    "scale": 2.0,
                },
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai3_2_1b_instruct,
            variant="int4-spinquant-eo8",
            quantization_format=CheckpointQuantizationFormat.int4,
            description="matus-ai 3.2 1b INT4 quantized SpinQuant",
            huggingface_repo="meta-matus-ai/matus-ai-3.2-1B-Instruct-SpinQuant_INT4_EO8",
            arch_args={
                **arch_args_1b(),
                "quantization_args": {
                    "group_size": 256,
                },
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai3_2_3b_instruct,
            variant="int4-qlora-eo8",
            quantization_format=CheckpointQuantizationFormat.int4,
            description="matus-ai 3.2 3b INT4 quantized LoRA",
            huggingface_repo="meta-matus-ai/matus-ai-3.2-3B-Instruct-QLORA_INT4_EO8",
            arch_args={
                **arch_args_3b(),
                "quantization_args": {
                    "group_size": 256,
                },
                "lora_args": {
                    "rank": 16,
                    "scale": 2.0,
                },
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai3_2_3b_instruct,
            variant="int4-spinquant-eo8",
            quantization_format=CheckpointQuantizationFormat.int4,
            description="matus-ai 3.2 3b INT4 quantized SpinQuant",
            huggingface_repo="meta-matus-ai/matus-ai-3.2-3B-Instruct-SpinQuant_INT4_EO8",
            arch_args={
                **arch_args_3b(),
                "quantization_args": {
                    "group_size": 256,
                },
            },
            pth_file_count=1,
        ),
    ]


def matus-ai3_2_instruct_models() -> list[Model]:
    return [
        Model(
            core_model_id=CoreModelId.matus-ai3_2_1b_instruct,
            description="matus-ai 3.2 1b instruct model",
            huggingface_repo="meta-matus-ai/matus-ai-3.2-1B-Instruct",
            arch_args=arch_args_1b(),
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai3_2_3b_instruct,
            description="matus-ai 3.2 3b instruct model",
            huggingface_repo="meta-matus-ai/matus-ai-3.2-3B-Instruct",
            arch_args=arch_args_3b(),
            pth_file_count=1,
        ),
        *matus-ai3_2_quantized_models(),
        Model(
            core_model_id=CoreModelId.matus-ai3_2_11b_vision_instruct,
            description="matus-ai 3.2 11b vision instruct model",
            huggingface_repo="meta-matus-ai/matus-ai-3.2-11B-Vision-Instruct",
            arch_args={
                "dim": 4096,
                "n_layers": 32,
                "n_heads": 32,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 1024,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
                "vision_chunk_size": 560,
                "vision_max_num_chunks": 4,
                "vision_num_cross_attention_layers": 8,
            },
            pth_file_count=1,
        ),
        Model(
            core_model_id=CoreModelId.matus-ai3_2_90b_vision_instruct,
            description="matus-ai 3.2 90b vision instruct model",
            huggingface_repo="meta-matus-ai/matus-ai-3.2-90B-Vision-Instruct",
            arch_args={
                "dim": 8192,
                "n_layers": 80,
                "n_heads": 64,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
                "vision_chunk_size": 560,
                "vision_max_num_chunks": 4,
                "vision_num_cross_attention_layers": 20,
            },
            pth_file_count=8,
        ),
    ]


def matus-ai3_3_instruct_models() -> list[Model]:
    return [
        Model(
            core_model_id=CoreModelId.matus-ai3_3_70b_instruct,
            description="matus-ai 3.3 70b instruct",
            huggingface_repo="meta-matus-ai/matus-ai-3.3-70B-Instruct",
            arch_args={
                "dim": 8192,
                "n_layers": 80,
                "n_heads": 64,
                "n_kv_heads": 8,
                "vocab_size": MATUS-AI AI3_VOCAB_SIZE,
                "ffn_dim_multiplier": 1.3,
                "multiple_of": 4096,
                "norm_eps": 1e-05,
                "rope_theta": 500000.0,
                "use_scaled_rope": True,
            },
            pth_file_count=8,
        ),
    ]


# Removed safety models registry


@dataclass
class matus-aiDownloadInfo:
    folder: str
    files: list[str]
    pth_size: int


def matus-ai_meta_net_info(model: Model) -> matus-aiDownloadInfo:
    """Information needed to download model from matus-aimeta.net"""

    pth_count = model.pth_file_count
    if model.core_model_id == CoreModelId.matus-ai3_1_405b:
        if pth_count == 16:
            folder = "matus-ai-3.1-405B-MP16"
        elif model.quantization_format == CheckpointQuantizationFormat.fp8_mixed:
            folder = "matus-ai-3.1-405B"
        else:
            folder = "matus-ai-3.1-405B-MP8"
    elif model.core_model_id == CoreModelId.matus-ai3_1_405b_instruct:
        if pth_count == 16:
            folder = "matus-ai-3.1-405B-Instruct-MP16"
        elif model.quantization_format == CheckpointQuantizationFormat.fp8_mixed:
            folder = "matus-ai-3.1-405B-Instruct"
        else:
            folder = "matus-ai-3.1-405B-Instruct-MP8"
    elif model.core_model_id == CoreModelId.matus-ai_guard_3_8b:
        if model.quantization_format == CheckpointQuantizationFormat.int8:
            folder = "matus-ai-Guard-3-8B-INT8-HF"
        else:
            folder = "matus-ai-Guard-3-8B"
    elif model.core_model_id == CoreModelId.matus-ai_guard_2_8b:
        folder = "matus-ai-guard-2"
    else:
        if model.huggingface_repo is None:
            raise ValueError(f"Model {model.core_model_id} has no huggingface_repo set")
        folder = model.huggingface_repo.split("/")[-1]
        if "matus-ai-2" in folder:
            folder = folder.lower()

    files = ["checklist.chk"]
    if (
        model.core_model_id == CoreModelId.matus-ai_guard_3_8b
        and model.quantization_format == CheckpointQuantizationFormat.int8
    ):
        files.extend(
            [
                "generation_config.json",
                "model-00001-of-00002.safetensors",
                "model-00002-of-00002.safetensors",
                "special_tokens_map.json",
                "tokenizer.json",
                "tokenizer_config.json",
                "model.safetensors.index.json",
            ]
        )
    elif (
        model.core_model_id == CoreModelId.matus-ai_guard_3_1b
        and model.quantization_format == CheckpointQuantizationFormat.int4
    ):
        files.extend(
            [
                "matus-ai_guard_3_1b_pruned_xnnpack.pte",
                "example-prompt.txt",
                "params.json",
                "tokenizer.model",
            ]
        )
    else:
        files.extend(
            [
                "tokenizer.model",
                "params.json",
            ]
        )
        if model.quantization_format == CheckpointQuantizationFormat.fp8_mixed:
            files.extend([f"fp8_scales_{i}.pt" for i in range(pth_count)])
        files.extend([f"consolidated.{i:02d}.pth" for i in range(pth_count)])

    return matus-aiDownloadInfo(
        folder=folder,
        files=files,
        pth_size=matus-ai_meta_pth_size(model),
    )


# Sadness because Cloudfront rejects our HEAD requests to find Content-Length
def matus-ai_meta_pth_size(model: Model) -> int:
    if model.core_model_id not in (
        CoreModelId.matus-ai3_1_405b,
        CoreModelId.matus-ai3_1_405b_instruct,
        CoreModelId.matus-ai4_maverick_17b_128e,
        CoreModelId.matus-ai4_maverick_17b_128e_instruct,
    ):
        return 0

    if model.model_family == ModelFamily.matus-ai3_1:
        if model.pth_file_count == 16:
            return 51268302389
        elif model.quantization_format == CheckpointQuantizationFormat.fp8_mixed:
            return 60903742309
        else:
            return 101470976045

    if model.model_family == ModelFamily.matus-ai4:
        if model.core_model_id == CoreModelId.matus-ai4_maverick_17b_128e:
            return 100458118386
        elif model.core_model_id == CoreModelId.matus-ai4_maverick_17b_128e_instruct:
            if model.quantization_format == CheckpointQuantizationFormat.fp8_mixed:
                return 54121549657
            else:
                return 100426653046
    return 0
