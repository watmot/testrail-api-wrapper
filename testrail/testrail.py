from testrail.models.case import CaseModel
from testrail.models.case_type import CaseTypeModel
from testrail.models.entry import EntryModel
from testrail.models.milestone import MilestoneModel
from testrail.models.plan import PlanModel
from testrail.models.project import ProjectModel
from testrail.models.run import RunModel
from testrail.models.section import SectionModel
from testrail.models.suite import SuiteModel
from testrail.models.test import TestModel

from testrail.collections.case import CaseCollection
from testrail.collections.case_type import CaseTypeCollection
from testrail.collections.entry import EntryCollection
from testrail.collections.milestone import MilestoneCollection
from testrail.collections.plan import PlanCollection
from testrail.collections.project import ProjectCollection
from testrail.collections.run import RunCollection
from testrail.collections.section import SectionCollection
from testrail.collections.suite import SuiteCollection
from testrail.collections.test import TestCollection


class Testrail:
    @staticmethod
    def case(case_id=None):
        return CaseModel(case_id=case_id) if case_id else CaseModel()

    @staticmethod
    def cases(project_id=None, suite_id=None, section_id=None, limit=None, offset=None, filter=None, **parameters):
        return CaseCollection(project_id=project_id, suite_id=suite_id, section_id=section_id, limit=limit,
                              offset=offset, filter=filter, **parameters)

    @staticmethod
    def case_types():
        return CaseTypeCollection()

    @staticmethod
    def milestone(milestone_id=None):
        return MilestoneModel(milestone_id=milestone_id) if milestone_id else MilestoneModel()

    @staticmethod
    def milestones(project_id=None, is_completed=None, is_started=None, **parameters):
        return MilestoneCollection(project_id=project_id, is_completed=is_completed, is_started=is_started,
                                   **parameters)

    @staticmethod
    def plan(plan_id=None):
        return PlanModel(plan_id=plan_id) if plan_id else PlanModel()

    @staticmethod
    def plans(project_id=None, created_after=None, created_before=None, created_by=None, is_completed=None,
              limit=None, offset=None, milestone_id=None, **parameters):
        return PlanCollection(project_id=project_id, created_after=created_after, created_before=created_before,
                              created_by=created_by, is_completed=is_completed, limit=limit, offset=offset,
                              milestone_id=milestone_id, **parameters)

    @staticmethod
    def project(project_id=None):
        return ProjectModel(project_id=project_id) if project_id else ProjectModel()

    @staticmethod
    def projects(is_completed=None, **parameters):
        return ProjectCollection(is_completed=is_completed, **parameters)

    @staticmethod
    def run(run_id=None):
        return RunModel(run_id=run_id) if run_id else RunModel()

    @staticmethod
    def runs(project_id=None, created_after=None, created_before=None, created_by=None, is_completed=None, limit=None,
             offset=None, milestone_id=None, suite_id=None, **parameters):
        return RunCollection(project_id=project_id, created_after=created_after, created_before=created_before,
                             created_by=created_by, is_completed=is_completed, limit=limit, offset=offset,
                             milestone_id=milestone_id, suite_id=suite_id, **parameters)

    @staticmethod
    def section(section_id=None):
        return SectionModel(section_id=section_id) if section_id else SectionModel()

    @staticmethod
    def sections(project_id=None, suite_id=None, **parameters):
        return SectionCollection(project_id=project_id, suite_id=suite_id, **parameters)

    @staticmethod
    def suite(suite_id=None):
        return SuiteModel(suite_id=suite_id) if suite_id else SuiteModel()

    @staticmethod
    def suites(project_id=None, **parameters):
        return SuiteCollection(project_id=project_id, **parameters)

    # @staticmethod
    # def entry(plan_id=None, entry_id=None):
    #     entry = None
    #
    #     if plan_id and entry_id:
    #         plan = PlanModel(plan_id=plan_id)
    #         try:
    #             entries = plan['entries']
    #             for entry in entries:
    #                 if entry['id'] == entry_id:
    #                     entry = e
    #         except KeyError as ex:
    #             logging.warning(ex)
    #     elif not plan_id or not entry_id:
    #         logging.warning(msg='Need both plan_id and entry_id.')
    #
    #     return EntryModel(response=entry)
    #
    # @staticmethod
    # def entries(plan_id=None):
    #     entries = None
    #
    #     if plan_id:
    #         plan = PlanModel(plan_id=plan_id)
    #         try:
    #             entries = plan['entries']
    #         except KeyError as ex:
    #             logging.warning(ex)
    #
    #     return EntryCollection(response=entries)
    #
    # @staticmethod
    # def test(test_id=None):
    #     return TestModel(test_id=test_id)
    #
    # @staticmethod
    # def tests(run_id=None, **parameters):
    #     return TestCollection(run_id=run_id, params=request_params(**parameters))
