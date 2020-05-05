import pytest
import random

from testrail import Testrail


@pytest.mark.skip()
class TestEntry:
    def test_get_entries(self, plan, entry):
        entries = Testrail.entries(plan_id=plan.id)
        index = random.randint(0, len(entries) - 1)
        assert entries[index].id

    def test_get_entry(self, entry):
        get_entry = Testrail.entry(plan_id=entry.plan_id, entry_id=entry.id)
        assert get_entry.id

    def test_add_entry(self, entry):
        assert entry.id
