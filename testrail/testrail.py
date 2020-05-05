from testrail.models.case import CaseModel
from testrail.models.case_field import CaseFieldModel
from testrail.models.case_type import CaseTypeModel
from testrail.models.entry import EntryModel
from testrail.models.milestone import MilestoneModel
from testrail.models.plan import PlanModel
from testrail.models.project import ProjectModel
from testrail.models.result_field import ResultFieldModel
from testrail.models.run import RunModel
from testrail.models.section import SectionModel
from testrail.models.suite import SuiteModel
from testrail.models.template import TemplateModel
from testrail.models.test import TestModel
from testrail.models.user import UserModel

from testrail.collections.case import CaseCollection
from testrail.collections.case_field import CaseFieldCollection
from testrail.collections.case_type import CaseTypeCollection
from testrail.collections.entry import EntryCollection
from testrail.collections.milestone import MilestoneCollection
from testrail.collections.plan import PlanCollection
from testrail.collections.priority import PriorityCollection
from testrail.collections.project import ProjectCollection
from testrail.collections.report import ReportCollection
from testrail.collections.result_field import ResultFieldCollection
from testrail.collections.run import RunCollection
from testrail.collections.section import SectionCollection
from testrail.collections.status import StatusCollection
from testrail.collections.suite import SuiteCollection
from testrail.collections.template import TemplateCollection
from testrail.collections.test import TestCollection
from testrail.collections.user import UserCollection


class Testrail:
    @staticmethod
    def case(case_id=None):
        return CaseModel(case_id=case_id) if case_id else CaseModel()

    @staticmethod
    def cases(project_id=None, suite_id=None, section_id=None, limit=None, offset=None, filter=None, **parameters):
        return CaseCollection(project_id=project_id, suite_id=suite_id, section_id=section_id, limit=limit,
                              offset=offset, filter=filter, **parameters)

    @staticmethod
    def case_field():
        return CaseFieldModel()

    @staticmethod
    def case_fields(**parameters):
        return CaseFieldCollection(**parameters)

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
    def priorities(**parameters):
        return PriorityCollection(**parameters)

    @staticmethod
    def project(project_id=None):
        return ProjectModel(project_id=project_id) if project_id else ProjectModel()

    @staticmethod
    def projects(is_completed=None, **parameters):
        return ProjectCollection(is_completed=is_completed, **parameters)

    @staticmethod
    def reports(project_id=None, **parameters):
        return ReportCollection(project_id=project_id, **parameters)

    @staticmethod
    def result_fields(**parameters):
        return ResultFieldCollection(**parameters)

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
    def statuses(**parameters):
        return StatusCollection(**parameters)

    @staticmethod
    def suite(suite_id=None):
        return SuiteModel(suite_id=suite_id) if suite_id else SuiteModel()

    @staticmethod
    def suites(project_id=None, **parameters):
        return SuiteCollection(project_id=project_id, **parameters)

    @staticmethod
    def templates(project_id=None, **parameters):
        return TemplateCollection(project_id=project_id, **parameters)

    @staticmethod
    def user(user_id=None):
        return UserModel(user_id=user_id) if user_id else UserModel()

    @staticmethod
    def users(**parameters):
        return UserCollection(**parameters)

    @staticmethod
    def test(test_id=None):
        return TestModel(test_id=test_id)

    @staticmethod
    def tests(run_id=None, **parameters):
        return TestCollection(run_id=run_id, **parameters)
