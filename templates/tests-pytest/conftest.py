import pytest
import os


@pytest.fixture(scope="function")
def change_base_dir():
    """Change dir to the base of the repo."""
    os.chdir(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))


@pytest.fixture()
def fixture_paths():
    """Change to the fixtures dir in the current directory of the test."""
    dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "fixtures")
    return [os.path.join(dir, i) for i in os.listdir(dir)]


@pytest.fixture()
def fixture_dir():
    """Path to fixtures dir from test file."""
    dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "fixtures")
    return dir
