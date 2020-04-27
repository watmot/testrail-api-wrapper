import random

from testrail import Testrail


class TestPlan:
    def test_get_plans(self, project, plan):
        plans = Testrail.plans(project_id=project.id)
        index = random.randint(0, len(plans)-1)

        assert plans[index].id

    def test_get_plan(self, plan):
        get_plan = Testrail.plan(plan_id=plan.id)

        assert get_plan.id

    def test_add_plan(self, plan):
        assert plan.id

    def test_update_plan(self, plan, test_plan_data):
        updated_plan_data = test_plan_data['updated']

        plan.name = updated_plan_data['name']
        plan.update()

        assert plan.name == updated_plan_data['name']

    def test_close_plan(self, plan):
        plan.close()

        assert plan.is_completed

    def test_delete_plan(self, plan):
        deleted_plan = plan.delete()

        assert deleted_plan.status_code == 200
