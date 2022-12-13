from tackle import tackle

{% if tackle_file == 'code-generation.yaml' %}
def test_default(
        change_base_dir,
        assert_paths,
        change_dir,{% if tests_enable and tests.type == 'pytest' %}
        test_pytest_output, {% else %}test_unittest_output, {% endif %}
        cleanup_path,
):
    """Test the default choices."""
    overrides = {
        "project_name": "output",
        "project_slug": "output",
        "author": "foo",
        "org": "bar",
        "license": "",  # Disables prompting for license
    }

    tackle(no_input=True, override=overrides)

    assert_paths([
        'README.md',
        'requirements-dev.txt',
        '.pre-commit-config.yaml',
    ], ".")

    cleanup_path("output")


{% endif %}{% if tackle_file == 'cli.yaml' %}
def test_default(
        change_base_dir,
):
    """Test the default choices."""
    overrides = {
        "hook_field": "foo",
        "license": "",  # Disables prompting for license
    }
    output = tackle(no_input=True, override=overrides)

    assert output

{% endif %}

