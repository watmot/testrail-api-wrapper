import random

from testrail import Testrail


class TestTemplate:
    def test_get_result_fields(self):
        result_fields = Testrail.result_fields()
        index = random.randint(0, len(result_fields)-1)

        assert result_fields[index].id

