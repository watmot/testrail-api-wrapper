import random
import pytest

from testrail import Testrail


@pytest.mark.skip
class TestReport:
    def test_get_reports(self, project, run):
        reports = Testrail.reports(project_id=project.id)
        index = random.randint(0, len(runs)-1)
        assert runs[index].id
