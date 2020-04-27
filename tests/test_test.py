import random

from testrail import Testrail
from testrail.models.test import TestModel


class TestTest:
    def test_get_tests(self, run):
        tests = Testrail.tests(run_id=run.id)
        index = random.randint(0, len(tests)-1)

        assert isinstance(tests[index], TestModel)

    def test_get_test(self, run):
        tests = Testrail.tests(run_id=run.id)
        get_test = Testrail.test(test_id=tests[0].id)

        assert isinstance(get_test, TestModel)
