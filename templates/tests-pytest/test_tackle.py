from tackle.main import tackle
import os
import yaml


def test_min(change_base_dir, fixture_dir):
    fixture = os.path.join(fixture_dir, "min.yaml")
    with open(fixture) as f:
        fixture_dict = yaml.safe_load(f)
    create = tackle(**fixture_dict, no_input=True)
    assert len(create["demo"]) == 0


def test_monty(change_base_dir, fixture_dir):
    fixture = os.path.join(fixture_dir, "monty.yaml")
    create = tackle(overwrite_inputs=fixture, no_input=True)
    assert len(create["demo"]) == 1
    assert create["do_demo"][0]["name"] == "stuff"


def test_providers(change_base_dir, fixture_dir):
    fixture = os.path.join(fixture_dir, "providers.yaml")
    create = tackle(overwrite_inputs=fixture, no_input=True)
    assert len(create["demo"]) == 1


def test_jinja(change_base_dir, fixture_dir):
    fixture = os.path.join(fixture_dir, "jinja.yaml")
    create = tackle(overwrite_inputs=fixture, no_input=True)
    assert len(create["demo"]) == 1


def test_embedded(change_base_dir, fixture_dir):
    fixture = os.path.join(fixture_dir, "embedded.yaml")
    create = tackle(overwrite_inputs=fixture, no_input=True)
    assert len(create["demo"]) == 1
