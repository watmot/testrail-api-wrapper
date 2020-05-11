import random

from testrail import Testrail


class TestStatus:
    def test_get_statuses(self):
        statuses = Testrail.statuses()
        statuses.get()
        index = random.randint(0, len(statuses)-1)

        assert statuses[index].id

