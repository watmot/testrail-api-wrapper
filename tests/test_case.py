import random

from testrail import Testrail


class TestCase:
    def test_get_cases(self, suite, case):
        cases = Testrail.cases()
        cases.get(project_id=suite.project_id, suite_id=suite.id)
        index = random.randint(0, len(cases)-1)

        assert cases[index].id

    def test_get_case(self, case):
        get_case = Testrail.case()
        get_case.get(case_id=case.id)

        assert get_case.id

    def test_add_case(self, case):
        assert case.id

    def test_update_case(self, case, test_case_data):
        updated_case_data = test_case_data['updated']

        case.title = updated_case_data['title']
        case.update()

        assert case.title == updated_case_data['title']

    def test_delete_case(self, case):
        deleted_case = case.delete()

        assert deleted_case.status_code == 200
