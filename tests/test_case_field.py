import random

from testrail import Testrail


class TestCase:
    def test_get_case_fields(self):
        cases = Testrail.case_fields()
        index = random.randint(0, len(cases)-1)

        assert cases[index].id

    def test_add_case_field(self, case):
        assert case.id
