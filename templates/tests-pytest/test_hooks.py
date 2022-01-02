from tackle import tackle
import os
import yaml


def test_min(change_base_dir, fixture_dir):
    fixture = os.path.join(fixture_dir, "min.yaml")
    with open(fixture) as f:
        fixture_dict = yaml.safe_load(f)
    create = tackle(**fixture_dict, no_input=True)
    assert len(create["demo"]) == 0
