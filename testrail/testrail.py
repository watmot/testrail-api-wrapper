from testrail.models.case import CaseModel
from testrail.models.case_field import CaseFieldModel
from testrail.models.case_type import CaseTypeModel
from testrail.models.entry import EntryModel
from testrail.models.milestone import MilestoneModel
from testrail.models.plan import PlanModel
from testrail.models.project import ProjectModel
from testrail.models.result import ResultModel
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
from testrail.collections.result import ResultCollection
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
    def case(case_id=None, new=False):
        return CaseModel(case_id=case_id, new=new)

    @staticmethod
    def cases(project_id=None, suite_id=None, section_id=None, limit=None, offset=None, filter=None, new=False,
              **parameters):
        return CaseCollection(project_id=project_id, suite_id=suite_id, section_id=section_id, limit=limit,
                              offset=offset, filter=filter, new=new, **parameters)

    @staticmethod
    def case_field(new=False):
        return CaseFieldModel(new=new)

    @staticmethod
    def case_fields(new=False, **parameters):
        return CaseFieldCollection(new=new, **parameters)

    @staticmethod
    def case_types(new=False):
        return CaseTypeCollection(new=new)

    @staticmethod
    def milestone(milestone_id=None, new=False):
        return MilestoneModel(milestone_id=milestone_id, new=new)

    @staticmethod
    def milestones(project_id=None, is_completed=None, is_started=None, new=False, **parameters):
        return MilestoneCollection(project_id=project_id, is_completed=is_completed, is_started=is_started, new=new,
                                   **parameters)

    @staticmethod
    def plan(plan_id=None, new=False):
        return PlanModel(plan_id=plan_id, new=new)

    @staticmethod
    def plans(project_id=None, created_after=None, created_before=None, created_by=None, is_completed=None,
              limit=None, offset=None, milestone_id=None, new=False, **parameters):
        return PlanCollection(project_id=project_id, created_after=created_after, created_before=created_before,
                              created_by=created_by, is_completed=is_completed, limit=limit, offset=offset,
                              milestone_id=milestone_id, new=new, **parameters)

    @staticmethod
    def priorities(new=False, **parameters):
        return PriorityCollection(new=new, **parameters)

    @staticmethod
    def project(project_id=None, new=False):
        return ProjectModel(project_id=project_id, new=new)

    @staticmethod
    def projects(is_completed=None, new=False, **parameters):
        return ProjectCollection(is_completed=is_completed, new=new, **parameters)

    @staticmethod
    def reports(project_id=None, new=False, **parameters):
        return ReportCollection(project_id=project_id, new=new, **parameters)

    @staticmethod
    def results(test_id=None, run_id=None, case_id=None, new=False, **parameters):
        return ResultCollection(test_id=test_id, run_id=run_id, case_id=case_id, new=new, **parameters)

    @staticmethod
    def result_fields(new=False, **parameters):
        return ResultFieldCollection(new=new, **parameters)

    @staticmethod
    def run(run_id=None, new=False):
        return RunModel(run_id=run_id, new=new)

    @staticmethod
    def runs(project_id=None, created_after=None, created_before=None, created_by=None, is_completed=None, limit=None,
             offset=None, milestone_id=None, suite_id=None, new=False, **parameters):
        return RunCollection(project_id=project_id, created_after=created_after, created_before=created_before,
                             created_by=created_by, is_completed=is_completed, limit=limit, offset=offset,
                             milestone_id=milestone_id, suite_id=suite_id, new=new, **parameters)

    @staticmethod
    def section(section_id=None, new=False):
        return SectionModel(section_id=section_id, new=new)

    @staticmethod
    def sections(project_id=None, suite_id=None, new=False, **parameters):
        return SectionCollection(project_id=project_id, suite_id=suite_id, new=new, **parameters)

    @staticmethod
    def statuses(new=False, **parameters):
        return StatusCollection(new=new, **parameters)

    @staticmethod
    def suite(suite_id=None, new=False):
        return SuiteModel(suite_id=suite_id, new=new)

    @staticmethod
    def suites(project_id=None, new=False, **parameters):
        return SuiteCollection(project_id=project_id, new=new, **parameters)

    @staticmethod
    def templates(project_id=None, new=False, **parameters):
        return TemplateCollection(project_id=project_id, new=new, **parameters)

    @staticmethod
    def user(user_id=None, email=None, new=False):
        return UserModel(user_id=user_id, email=email, new=new)

    @staticmethod
    def users(new=False, **parameters):
        return UserCollection(new=new, **parameters)

    # @staticmethod
    # def test(test_id=None, new=False):
    #     return TestModel(test_id=test_id, new=new)
    #
    # @staticmethod
    # def tests(run_id=None, new=False, **parameters):
    #     return TestCollection(run_id=run_id, new=new, **parameters)
