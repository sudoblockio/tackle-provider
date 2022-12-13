from tackle.main import tackle
import os

BASE_OVERRIDES = {
    "project_name": "output",
    "project_slug": "output",
    "description": "A thing doer.",
    "author": {
        "name": "Bart",
        "email": "bart@simpson.com",
    },
    "repo_owner": "",
    "default_branch": "main",
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


PYTEST_OPTIONS = {
    "tests_enable": True,
    "tests": {
        "type": "pytest",
        "tox_enable": True,
        "ci_enable": True,
        "ci": {
            "type": "github",
            "platforms": ["ubuntu", "macos", "windows"],
            "python_versions": ["3.7", "3.9", "3.8", "3.10"],
            "use_foresight": True,
        },
    },
}


def test_pytest_cli(
    change_base_dir,
    assert_paths,
    cleanup_output,
    test_pytest_output,
):
    overrides = {
        "tackle_file": "cli.yaml",
        "hooks_enable": False,
    }
    overrides.update(BASE_OVERRIDES)
    overrides.update(PYTEST_OPTIONS)  # noqa

    tackle(no_input=True, override=overrides)

    test_pytest_output("output")

    assert_paths(
        [
            os.path.join("tests", "conftest.py"),
            ".tackle.yaml",
        ],
        "output",
    )


def test_pytest_code_gen(
    change_base_dir,
    assert_paths,
    cleanup_output,
    test_pytest_output,
):
    overrides = {
        "tackle_file": "code-generation.yaml",
        "hooks_enable": False,
    }
    overrides.update(BASE_OVERRIDES)
    overrides.update(PYTEST_OPTIONS)  # noqa

    tackle(no_input=True, override=overrides)

    test_pytest_output("output")

    assert_paths(
        [
            os.path.join("tests", "conftest.py"),
            ".tackle.yaml",
        ],
        "output",
    )


def test_pytest_no_tackle(
    change_base_dir,
    assert_paths,
    cleanup_output,
    test_pytest_output,
):
    overrides = {
        "tackle_file": "none",
        "hooks_enable": True,
        "hooks": {
            "type": "thing",
            "class_name": "ThingHook",
        },
    }
    overrides.update(BASE_OVERRIDES)
    overrides.update(PYTEST_OPTIONS)  # noqa

    tackle(no_input=True, override=overrides)

    # test_pytest_output("output")

    assert_paths(
        [
            os.path.join("tests", "conftest.py"),
        ],
        "output",
    )
