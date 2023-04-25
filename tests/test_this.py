from tackle import tackle
import os

BASE_OVERRIDES = {
    "project_name": "output",
    "project_slug": "output",
    "license": "",
}


def test_default(
    change_base_dir,
    assert_paths,
    change_dir,
    test_pytest_output,
    cleanup_output,
):
    """Test the default choices."""
    overrides = {
        "tackle_file": "none",
        "hooks_enable": False,
        "tests_enable": False,
    }
    overrides.update(BASE_OVERRIDES)
    tackle(no_input=True, override=overrides)
    assert_paths(
        [
            "README.md",
            "requirements-dev.txt",
            ".pre-commit-config.yaml",
        ],
        overrides["project_slug"],
    )


def test_cli(
    change_base_dir,
    assert_paths,
    cleanup_output,
    test_pytest_output,
):
    """Test creating a CLI app."""
    overrides = {
        "tackle_file": "cli.yaml",
        "hooks_enable": False,
    }
    overrides.update(BASE_OVERRIDES)
    tackle(no_input=True, override=overrides)
    test_pytest_output("output")
    assert_paths(
        [
            os.path.join("tests", "conftest.py"),
            ".tackle.yaml",
        ],
        "output",
    )


def test_code_gen(
    change_base_dir,
    assert_paths,
    cleanup_output,
    test_pytest_output,
):
    """Test creating a code generator."""
    overrides = {
        "tackle_file": "code-generation.yaml",
        "hooks_enable": False,
    }
    overrides.update(BASE_OVERRIDES)
    tackle(no_input=True, override=overrides)
    test_pytest_output("output")
    assert_paths(
        [
            os.path.join("tests", "conftest.py"),
            ".tackle.yaml",
        ],
        "output",
    )


def test_no_tackle(
    change_base_dir,
    assert_paths,
    cleanup_output,
    test_pytest_output,
):
    """Test creating a bare provider with only hooks."""
    overrides = {
        "tackle_file": "none",
        "hooks_enable": True,
        "hooks": {
            "type": "thing",
        },
    }
    overrides.update(BASE_OVERRIDES)
    tackle(no_input=True, override=overrides)
    test_pytest_output("output")
    assert_paths(
        [
            os.path.join("tests", "conftest.py"),
            os.path.join("tests", "fixtures"),
        ],
        "output",
    )
