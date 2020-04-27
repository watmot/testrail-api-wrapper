import random

from testrail import Testrail
from testrail.models.suite import SuiteModel


class TestSuite:
    def test_get_suites(self, project, suite):
        suites = Testrail.suites(project_id=project.id)
        index = random.randint(0, len(suites)-1)

        assert isinstance(suites[index], SuiteModel)

    def test_get_suite(self, suite):
        get_suite = Testrail.suite(suite_id=suite.id)

        assert isinstance(get_suite, SuiteModel)

    def test_add_suite(self, suite):
        assert suite.id

    def test_update_suite(self, suite, test_suite_data):
        updated_suite_data = test_suite_data['updated']

        suite.name = updated_suite_data['name']
        suite.update()

        assert suite.name == updated_suite_data['name']

    def test_delete_suite(self, suite):
        deleted_suite = suite.delete()

        assert deleted_suite.status_code == 200
