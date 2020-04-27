import random

from testrail import Testrail


class TestMilestone:
    def test_get_milestones(self, project, milestone):
        milestones = Testrail.milestones(project_id=project.id)
        index = random.randint(0, len(milestones)-1)
        assert milestones[index].id

    def test_get_milestone(self, milestone):
        get_milestone = Testrail.milestone(milestone_id=milestone.id)

        assert get_milestone.id

    def test_add_milestone(self, milestone):
        assert milestone.id

    def test_update_milestone(self, milestone, test_milestone_data):
        updated_milestone_data = test_milestone_data['updated']

        milestone.is_completed = updated_milestone_data['is_completed']
        milestone.update()

        assert milestone.is_completed

    def test_delete_milestone(self, milestone):
        deleted_milestone = milestone.delete()

        assert deleted_milestone.status_code == 200
