{% if tests.type == 'pytest' %}
import os
import shutil
import sys
import pytest
from pytest import ExitCode


@pytest.fixture()
def base_dir():
    """Change dir to the base of the repo."""
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")


@pytest.fixture()
def change_dir():
    """Change to a dir argument."""
    def f(dir: str):
        os.chdir(dir)

    return f


@pytest.fixture()
def change_base_dir(base_dir):
    """Change dir to the base of the repo."""
    os.chdir(base_dir)


@pytest.fixture()
def fixture_dir():
    """Path to fixtures dir from test file."""
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), "fixtures")


@pytest.fixture()
def fixture_path(fixture_dir):
    """Function to get path to fixture in fixture dir from test file."""

    def f(fixture: str):
        return os.path.join(fixture_dir, fixture)

    return f

{% if tackle_file == 'code-generation.yaml' and  tests_enable %}
@pytest.fixture()
def test_pytest_output():
    """Run pytest tests from a given path."""

    def f(output_path):
        path = os.path.join(output_path, "tests")
        sys.path.append(path)
        exit_code = pytest.main([path])
        if exit_code != ExitCode.OK:
            raise Exception(exit_code)

    return f
{% endif %}


{% if tackle_file == 'code-generation.yaml' and tests_enable %}
@pytest.fixture()
def test_unittest_output():
    """Run unittest tests from a given path."""

    def f(output_path):
        path = os.path.join(output_path, "tests")
        sys.path.append(path)
        unittest.main(path)

    return f
{% endif %}


{% if tackle_file == 'code-generation.yaml' and  tests_enable %}
@pytest.fixture(scope="function")
def assert_paths():
    """Return a function that asserts paths exists."""

    def f(paths: list, base_dir: str = None):
        for file in paths:
            if base_dir is not None:
                file = os.path.join(base_dir, file)

            assert os.path.exists(file)

    return f


@pytest.fixture(scope="function")
def cleanup_path():
    """Return a function that removes a directory argument."""

    def f(path: str):
        if os.path.exists(path):
            shutil.rmtree(path)

    return f
{% endif %}
{% endif %}
