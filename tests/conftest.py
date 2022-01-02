import pytest
import os


@pytest.fixture(scope="function")
def change_base_dir():
    """Change dir to the base of the repo."""
    os.chdir(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
