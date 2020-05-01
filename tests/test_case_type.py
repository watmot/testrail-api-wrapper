import random

from testrail import Testrail


class TestCaseType:
    def test_get_case_types(self):
        case_types = Testrail.case_types()
        index = random.randint(0, len(case_types)-1)

        assert case_types[index].id

