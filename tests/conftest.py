import pytest
import os


@pytest.fixture(scope="function")
def change_base_dir():
    """Change dir to the base of the repo."""
    os.chdir(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))


@pytest.fixture(scope="function")
def assert_paths():
    """Return a function that asserts paths exists."""

    def f(paths: list):
        for file in paths:
            assert os.path.exists(file)

    return f
