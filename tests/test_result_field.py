import random
import pytest

from testrail import Testrail


@pytest.mark.skip
class TestTemplate:
    def test_get_result_fields(self):
        result_fields = Testrail.result_fields()
        result_fields.get()
        index = random.randint(0, len(result_fields)-1)

        assert result_fields[index].id

