import random

from testrail import Testrail


class TestProject:
    def test_get_projects(self):
        projects = Testrail.projects()
        projects.get()
        index = random.randint(0, len(projects)-1)
        assert projects[index].id

    def test_get_project(self, project):
        test_project = Testrail.project()
        test_project.get(project_id=project.id)

        assert test_project.id

    def test_add_project(self, project):
        assert project.id

    def test_update_project(self, project, test_project_data):
        updated_project_data = test_project_data['updated']

        project.is_completed = updated_project_data['is_completed']

        project.update()

        assert project.is_completed

    def test_delete_project(self, project):
        deleted_project = project.delete()

        assert deleted_project.status_code == 200
