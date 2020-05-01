import random

from testrail import Testrail


class TestPriority:
    def test_get_priorities(self):
        priorities = Testrail.priorities()
        index = random.randint(0, len(priorities)-1)

        assert priorities[index].id
