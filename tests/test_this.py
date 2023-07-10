from tackle import tackle
import os

KWARGS: dict = {
    "project_name": "output",
    "project_slug": "output",
    "description": "foo and bar",
    "author_name": "me",
    "author_email": "me@you.com",
    "repo_owner": "sudoblockio",
    "default_branch": "main",
    "tests_enable": False,
}

OVERRIDES: dict = {
    "license": "",  # Snub the license module since it is external
}

TEST_OVERRIDES = {
    "tests": {
        "tox_enable": True,
        "ci_enable": True,
        "ci": [
            "3.9",
        ],
    }
}


def test_default(
    change_base_dir,
    assert_paths,
    change_dir,
    test_pytest_output,
    cleanup_output,
):
    """Test the default choices."""
    kwargs = {
        "tackle_file": "none",
        "hooks_enable": False,
        "tests_enable": False,
    }
    overrides = {}
    KWARGS.update(kwargs)
    OVERRIDES.update(overrides)

    tackle(**KWARGS, no_input=True, override=OVERRIDES)
    assert_paths(
        [
            "README.md",
            "requirements-dev.txt",
            ".pre-commit-config.yaml",
        ],
        KWARGS["project_slug"],
    )


def test_cli(
    change_base_dir,
    assert_paths,
    cleanup_output,
    test_pytest_output,
):
    """Test creating a CLI app."""
    kwargs = {
        "tackle_file": "cli.yaml",
        "hooks_enable": False,
        "tests_enable": True,
    }
    KWARGS.update(kwargs)
    OVERRIDES.update(TEST_OVERRIDES)

    tackle(**KWARGS, override=OVERRIDES)
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
    kwargs = {
        "tackle_file": "code-generation.yaml",
        "hooks_enable": False,
        "tests_enable": True,
    }
    KWARGS.update(kwargs)
    OVERRIDES.update(TEST_OVERRIDES)

    tackle(**KWARGS, no_input=True, override=OVERRIDES)
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
    kwargs = {
        "tackle_file": "none",
        "hooks_enable": True,
        "tests_enable": True,
    }
    overrides = {
        "hooks": {
            "type": "thing",
        },
    }
    KWARGS.update(kwargs)
    OVERRIDES.update(overrides)
    OVERRIDES.update(TEST_OVERRIDES)

    tackle(**KWARGS, no_input=True, override=OVERRIDES)
    test_pytest_output("output")

    assert_paths(
        [
            os.path.join("tests", "conftest.py"),
            os.path.join("tests", "fixtures"),
        ],
        "output",
    )
