from typing import Any
from tackle.models import BaseHook, Field


class {{class_name}}(BaseHook):
    """Hook for ..."""

    hook_type: str = '{{type}}'
    input: Any = Field(None, description="")
    args: list = ['input']

    def execute(self):
        pass
