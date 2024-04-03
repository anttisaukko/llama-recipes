# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

from typing import List, Optional
from dataclasses import dataclass, field
from torch.utils.tensorboard import SummaryWriter

@dataclass
class tensorboard_config:
    train_summary_writer: SummaryWriter
    test_summary_write: SummaryWriter