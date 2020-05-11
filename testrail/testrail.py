from testrail.models.case import CaseModel
from testrail.models.case_field import CaseFieldModel
from testrail.models.case_type import CaseTypeModel
from testrail.models.config import ConfigModel
from testrail.models.config_group import ConfigGroupModel
from testrail.models.entry import EntryModel
from testrail.models.milestone import MilestoneModel
from testrail.models.plan import PlanModel
from testrail.models.project import ProjectModel
from testrail.models.priority import PriorityModel
from testrail.models.report import ReportModel
from testrail.models.result import ResultModel
from testrail.models.result_field import ResultFieldModel
from testrail.models.run import RunModel
from testrail.models.section import SectionModel
from testrail.models.status import StatusModel
from testrail.models.suite import SuiteModel
from testrail.models.template import TemplateModel
from testrail.models.test import TestModel
from testrail.models.user import UserModel

from testrail.collections.case import CaseCollection
from testrail.collections.case_field import CaseFieldCollection
from testrail.collections.case_type import CaseTypeCollection
from testrail.collections.config import ConfigCollection
from testrail.collections.config_group import ConfigGroupCollection
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
    def case():
        return CaseModel()

    @staticmethod
    def cases():
        return CaseCollection()

    @staticmethod
    def case_field():
        return CaseFieldModel()

    @staticmethod
    def case_fields():
        return CaseFieldCollection()

    @staticmethod
    def case_type():
        return CaseTypeModel()

    @staticmethod
    def case_types():
        return CaseTypeCollection()

    @staticmethod
    def config():
        return ConfigModel()

    @staticmethod
    def configs():
        return ConfigCollection()

    @staticmethod
    def config_group():
        return ConfigGroupModel()

    @staticmethod
    def config_groups():
        return ConfigGroupCollection()

    @staticmethod
    def entry():
        return EntryModel()

    @staticmethod
    def entries():
        return EntryCollection()

    @staticmethod
    def milestone():
        return MilestoneModel()

    @staticmethod
    def milestones():
        return MilestoneCollection()

    @staticmethod
    def plan():
        return PlanModel()

    @staticmethod
    def plans():
        return PlanCollection()

    @staticmethod
    def priority():
        return PriorityModel()

    @staticmethod
    def priorities():
        return PriorityCollection()

    @staticmethod
    def project():
        return ProjectModel()

    @staticmethod
    def projects():
        return ProjectCollection()

    @staticmethod
    def report():
        return ReportModel()

    @staticmethod
    def reports():
        return ReportCollection()

    @staticmethod
    def result():
        return ResultModel()

    @staticmethod
    def results():
        return ResultCollection()

    @staticmethod
    def result_field():
        return ResultFieldModel()

    @staticmethod
    def result_fields():
        return ResultFieldCollection()

    @staticmethod
    def run():
        return RunModel()

    @staticmethod
    def runs():
        return RunCollection()

    @staticmethod
    def section():
        return SectionModel()

    @staticmethod
    def sections():
        return SectionCollection()

    @staticmethod
    def status():
        return StatusModel()

    @staticmethod
    def statuses():
        return StatusCollection()

    @staticmethod
    def suite():
        return SuiteModel()

    @staticmethod
    def suites():
        return SuiteCollection()

    @staticmethod
    def template():
        return TemplateModel()

    @staticmethod
    def templates():
        return TemplateCollection()

    @staticmethod
    def test():
        return TestModel()

    @staticmethod
    def tests():
        return TestCollection()

    @staticmethod
    def user():
        return UserModel()

    @staticmethod
    def users():
        return UserCollection()
