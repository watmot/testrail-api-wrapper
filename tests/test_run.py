import random

from testrail import Testrail


class TestRun:
    def test_get_runs(self, project, run):
        runs = Testrail.runs(project_id=project.id)
        index = random.randint(0, len(runs)-1)
        assert runs[index].id

    def test_get_run(self, run):
        get_run = Testrail.run(run_id=run.id)
        assert get_run.id

    def test_add_run(self, run):
        assert run.id

    def test_update_run(self, run, test_run_data):
        updated_run_data = test_run_data['updated']

        run.name = updated_run_data['name']
        run.update()

        assert run.name == updated_run_data['name']

    def test_close_run(self, run):
        run.close()

        assert run.is_completed

    def test_delete_plan(self, run):
        deleted_run = run.delete()

        assert deleted_run.status_code == 200
