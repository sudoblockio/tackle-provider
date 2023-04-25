import unittest
import os
import shutil

from tackle import tackle


class TestTackleInputs(unittest.TestCase):
    def test_min(self):
        create = tackle(no_input=True)
        project_slug = "my-provider"
        assert os.path.exists(project_slug)
        assert create["project_slug"] == project_slug
        shutil.rmtree(project_slug)
