from tackle.main import tackle
import os
import shutil


def test_default(change_base_dir):
    """Test the default choices."""
    create = tackle(no_input=True)
    project_slug = "tackle-my-provider"
    assert os.path.exists(project_slug)
    assert create["project_slug"] == project_slug
    shutil.rmtree(project_slug)
