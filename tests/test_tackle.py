from tackle.main import tackle
import os
import shutil


def test_min(change_base_dir):
    create = tackle(no_input=True)
    assert os.path.exists("my-provider")
    assert len(create["demo"]) == 0
    shutil.rmtree("my-provider")
