import random

from testrail import Testrail


class TestTemplate:
    def test_get_templates(self, project):
        templates = Testrail.templates(project_id=project.id)
        index = random.randint(0, len(templates)-1)

        assert templates[index].id

