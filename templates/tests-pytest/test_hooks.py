import os
from tackle import tackle


def test_default(change_base_dir, fixture_dir):
    output = tackle(os.path.join(fixture_dir, "min.yaml"), no_input=True)
    assert output
