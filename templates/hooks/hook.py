"""{{project_name}} hooks."""
from typing import Any
from tackle.models import BaseHook, Field


class {{class_name}}(BaseHook):
    """Hook for ..."""

    hook_type: str = '{{type}}'
    input: Any = Field(None, description="Extra key to embed into. Artifact of API.")
    _args: list = ['input']

    def execute(self):
        pass