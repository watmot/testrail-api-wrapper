class AnnouncementMixin:
    @property
    def announcement(self):
        return self._data.get('announcement')

    @announcement.setter
    def announcement(self, arg):
        self._data['announcement'] = str(arg)


class AssignedToIdMixin:
    @property
    def assignedto_id(self):
        return self._data.get('assigned_to_id')

    @assignedto_id.setter
    def assignedto_id(self, arg):
        self._data['assigned_to_id'] = int(arg)


class BlockedCountMixin:
    @property
    def blocked_count(self):
        return self._data.get('blocked_count')


class CaseIdMixin:
    @property
    def case_id(self):
        return self._data.get('case_id')


class CaseIdsMixin:
    @property
    def case_ids(self):
        return self._data.get('case_ids')

    @case_ids.setter
    def case_ids(self, arg):
        ids = [case.id for case in arg]
        self._data['case_ids'] = ids


class CasesColumnsMixin:
    @property
    def cases_columns(self):
        return self._data.get('cases_columns')

    @cases_columns.setter
    def cases_columns(self, arg):
        self._data['cases_columns'] = arg


class CasesFiltersMixin:
    @property
    def cases_filters(self):
        return self._data.get('cases_filters')

    @cases_filters.setter
    def cases_filters(self, arg):
        self._data['cases_filters'] = arg


class CasesIncludeNewMixin:
    @property
    def cases_include_new(self):
        return self._data.get('cases_include_new')

    @cases_include_new.setter
    def cases_include_new(self, arg):
        self._data['cases_include_new'] = arg


class CasesIncludeUpdatedMixin:
    @property
    def cases_include_updated(self):
        return self._data.get('cases_include_updated')

    @cases_include_updated.setter
    def cases_include_updated(self, arg):
        self._data['cases_include_updated'] = arg


class CasesGroupByMixin:
    @property
    def cases_group_by(self):
        return self._data.get('cases_group_by')

    @cases_group_by.setter
    def cases_group_by(self, arg):
        self._data['cases_group_by'] = arg


class CasesLimitMixin:
    @property
    def cases_limit(self):
        return self._data.get('cases_limit')

    @cases_limit.setter
    def cases_limit(self, arg):
        self._data['cases_limit'] = arg


class ChangesDateRangeMixin:
    @property
    def changes_date_range(self):
        return self._data.get('changes_date_range')

    @changes_date_range.setter
    def changes_date_range(self, arg):
        self._data['changes_date_range'] = arg


class ChangesDateRangeFromMixin:
    @property
    def changes_date_range_from(self):
        return self._data.get('changes_date_range_from')

    @changes_date_range_from.setter
    def changes_date_range_from(self, arg):
        self._data['changes_date_range_from'] = arg


class ChangesDateRangeToMixin:
    @property
    def changes_date_range_to(self):
        return self._data.get('changes_date_range_to')

    @changes_date_range_to.setter
    def changes_date_range_to(self, arg):
        self._data['changes_date_range_to'] = arg


class ColorBrightMixin:
    @property
    def color_bright(self):
        return self._data.get('color_bright')


class ColorDarkMixin:
    @property
    def color_dark(self):
        return self._data.get('color_dark')


class ColorMediumMixin:
    @property
    def color_medium(self):
        return self._data.get('color_medium')


class CommentMixin:
    @property
    def comment(self):
        return self._data.get('comment')

    @comment.setter
    def comment(self, arg):
        self._data['comment'] = str(arg)


class CompletedOnMixin:
    @property
    def completed_on(self):
        return self._data.get('completed_on')


class ConfigMixin:
    @property
    def config(self):
        return self._data.get('config')


class ConfigIdsMixin:
    @property
    def config_ids(self):
        return self._data.get('config_ids')

    @config_ids.setter
    def config_ids(self, arg):
        self._data['config_ids'] = arg


class ConfigsMixin:
    @property
    def configs(self):
        return self._data.get('configs')


class ContentHideLinksMixin:
    @property
    def content_hide_links(self):
        return self._data.get('content_hide_links')

    @content_hide_links.setter
    def content_hide_links(self, arg):
        self._data['content_hide_links'] = arg


class CreatedByMixin:
    @property
    def created_by(self):
        return self._data.get('created_by')


class CreatedOnMixin:
    @property
    def created_on(self):
        return self._data.get('created_on')


class CustomStatus1CountMixin:
    @property
    def custom_status1_count(self):
        return self._data.get('custom_status1_count')


class CustomStatus2CountMixin:
    @property
    def custom_status2_count(self):
        return self._data.get('custom_status2_count')


class CustomStatus3CountMixin:
    @property
    def custom_status3_count(self):
        return self._data.get('custom_status3_count')


class CustomStatus4CountMixin:
    @property
    def custom_status4_count(self):
        return self._data.get('custom_status4_count')


class CustomStatus5CountMixin:
    @property
    def custom_status5_count(self):
        return self._data.get('custom_status5_count')


class CustomStatus6CountMixin:
    @property
    def custom_status6_count(self):
        return self._data.get('custom_status6_count')


class CustomStatus7CountMixin:
    @property
    def custom_status7_count(self):
        return self._data.get('custom_status7_count')


class CustomDescriptionMixin:
    @property
    def custom_description(self):
        return self._data.get('custom_description')


class CustomPreconditionMixin:
    @property
    def custom_precondition(self):
        return self._data.get('custom_precondition')


class CustomStepsMixin:
    @property
    def custom_steps(self):
        return self._data.get('custom_steps')


class CustomStepsSeparatedMixin:
    @property
    def custom_steps_separated(self):
        return self._data.get('custom_steps_separated')


class DefectsMixin:
    @property
    def defects(self):
        return self._data.get('defects')

    @defects.setter
    def defects(self, *args):
        arg = ' ,'.join(list(args))
        self._data['defects'] = arg


class DepthMixin:
    @property
    def depth(self):
        return self._data.get('depth')


class DescriptionMixin:
    @property
    def description(self):
        return self._data.get('description')

    @description.setter
    def description(self, arg):
        self._data['description'] = str(arg)


class DisplayOrderMixin:
    @property
    def display_order(self):
        return self._data.get('display_order')


class DueOnMixin:
    @property
    def due_on(self):
        return self._data.get('due_on')

    @due_on.setter
    def due_on(self, arg):
        self._data['due_on'] = int(arg)


class ElapsedMixin:
    @property
    def elapsed(self):
        return self._data.get('elapsed')

    @elapsed.setter
    def elapsed(self, arg):
        self._data['elapsed'] = str(arg)


class EmailMixin:
    @property
    def email(self):
        return self._data.get('email')


class EntriesMixin:
    @property
    def entries(self):
        return self._data.get('entries')


class EstimateMixin:
    @property
    def estimate(self):
        return self._data.get('estimate')

    @estimate.setter
    def estimate(self, arg):
        self._data['estimate'] = str(arg)


class EstimateForecastMixin:
    @property
    def estimate_forecast(self):
        return self._data.get('estimate_forecast')


class FailedCountMixin:
    @property
    def failed_count(self):
        return self._data.get('failed_count')


class GroupIdMixin:
    @property
    def group_id(self):
        return self._data.get('group_id')


class IdMixin:
    @property
    def id(self):
        return self._data.get('id')


class IncludeAllMixin:
    @property
    def include_all(self):
        return self._data.get('include_all')

    @include_all.setter
    def include_all(self, arg):
        self._data['include_all'] = True if bool(arg) else False


class IsActiveMixin:
    @property
    def is_active(self):
        return self._data.get('is_active')


class IsBaselineMixin:
    @property
    def is_baseline(self):
        return self._data.get('is_baseline')


class IsCompletedMixin:
    @property
    def is_completed(self):
        return self._data.get('is_completed')

    @is_completed.setter
    def is_completed(self, arg):
        self._data['is_completed'] = True if bool(arg) else False


class IsDefaultMixin:
    @property
    def is_default(self):
        return self._data.get('is_default')


class IsFinalMixin:
    @property
    def is_final(self):
        return self._data.get('is_final')


class IsMasterMixin:
    @property
    def is_master(self):
        return self._data.get('is_master')


class IsStartedMixin:
    @property
    def is_started(self):
        return self._data.get('is_started')

    @is_started.setter
    def is_started(self, arg):
        self._data['is_started'] = True if bool(arg) else False


class IsSystemMixin:
    @property
    def is_system(self):
        return self._data.get('is_system')


class IsUntestedMixin:
    @property
    def is_untested(self):
        return self._data.get('is_untested')


class LabelMixin:
    @property
    def label(self):
        return self._data.get('label')


class MilestoneIdMixin:
    @property
    def milestone_id(self):
        return self._data.get('milestone_id')


class MilestonesMixin:
    def milestones(self):
        return self._data.get('milestones')


class NameMixin:
    @property
    def name(self):
        return self._data.get('name')

    @name.setter
    def name(self, arg):
        self._data['name'] = arg


class NotifyUserMixin:
    @property
    def notify_user(self):
        return self._data.get('notify_user')

    @notify_user.setter
    def notify_user(self, arg):
        self._data['notify_user'] = arg


class NotifyLinkMixin:
    @property
    def notify_link(self):
        return self._data.get('notify_link')

    @notify_link.setter
    def notify_link(self, arg):
        self._data['notify_link'] = arg


class NotifyLinkRecipientsMixin:
    @property
    def notify_link_recipients(self):
        return self._data.get('notify_link_recipients')

    @notify_link_recipients.setter
    def notify_link_recipients(self, arg):
        self._data['notify_link_recipients'] = arg


class NotifyAttachmentMixin:
    @property
    def notify_attachment(self):
        return self._data.get('notify_attachment')

    @notify_attachment.setter
    def notify_attachment(self, arg):
        self._data['notify_attachment'] = arg


class NotifyAttachmentHTMLFormatMixin:
    @property
    def notify_attachment_html_format(self):
        return self._data.get('notify_attachment_html_format')

    @notify_attachment_html_format.setter
    def notify_attachment_html_format(self, arg):
        self._data['notify_attachment_html_format'] = arg


class NotifyAttachmentPDFFormatMixin:
    @property
    def notify_attachment_pdf_format(self):
        return self._data.get('notify_attachment_pdf_format(')

    @notify_attachment_pdf_format.setter
    def notify_attachment_pdf_format(self, arg):
        self._data['notify_attachment_pdf_format'] = arg


class ParentIdMixin:
    @property
    def parent_id(self):
        return self._data.get('parent_id')


class PassedCountMixin:
    @property
    def passed_count(self):
        return self._data.get('passed_count')


class PlanIdMixin:
    @property
    def plan_id(self):
        return self._data.get('plan_id')

    @plan_id.setter
    def plan_id(self, arg):
        self._data['plan_id'] = int(arg)


class PlatformMixin:
    @property
    def platform(self):
        return self._data.get('platform')

    @platform.setter
    def platform(self, arg):
        self._data['platform'] = str(arg)


class PriorityMixin:
    @property
    def priority(self):
        return self._data.get('priority')


class PriorityIdMixin:
    @property
    def priority_id(self):
        return self._data.get('priority_id')


class ProjectIdMixin:
    @property
    def project_id(self):
        return self._data.get('project_id')

    @project_id.setter
    def project_id(self, arg):
        self._data['project_id'] = arg


class RefsMixin:
    @property
    def refs(self):
        return self._data.get('refs')

    @refs.setter
    def refs(self, *args):
        arg = ' ,'.join(list(args))
        self._data['refs'] = arg


class RetestCountMixin:
    @property
    def retest_count(self):
        return self._data.get('retest_count')


class RunIdMixin:
    @property
    def run_id(self):
        return self._data.get('run_id')


class RunsMixin:
    @property
    def runs(self):
        return self


class SectionIdMixin:
    @property
    def section_id(self):
        return self._data.get('section_id')

    @section_id.setter
    def section_id(self, arg):
        self._data['section_id'] = arg

    @property
    def short_name(self):
        return self._data.get('short_name')


class ShortNameMixin:
    @property
    def short_name(self):
        return self._data.get('short_name')

    @short_name.setter
    def short_name(self, arg):
        self._data['short_name'] = arg


class ShowAnnouncementMixin:
    @property
    def show_announcement(self):
        return self._data.get('show_announcement')

    @show_announcement.setter
    def show_announcement(self, arg):
        self._data['show_announcement'] = True if bool(arg) else False


class StartOnMixin:
    @property
    def start_on(self):
        return self._data.get('start_on')

    @start_on.setter
    def start_on(self, arg):
        self._data['start_on'] = int(arg)


class StartedOnMixin:
    @property
    def started_on(self):
        return self._data.get('started_on')


class StatusIdMixin:
    @property
    def status_id(self):
        return self._data.get('status_id')

    @status_id.setter
    def status_id(self, arg):
        self._data['status_id'] = arg


class SuiteIdMixin:
    @property
    def suite_id(self):
        return self._data.get('suite_id')

    @suite_id.setter
    def suite_id(self, arg):
        self._data['suite_id'] = arg


class SuiteModeMixin:
    @property
    def suite_mode(self):
        return self._data.get('suite_mode')

    @suite_mode.setter
    def suite_mode(self, arg):
        modes = [1, 2, 3]
        if arg not in modes:
            raise ValueError('\'arg\' must be in {}'.format(modes))
        self._data['suite_mode'] = arg


class SuitesInclude:
    @property
    def suites_include(self):
        return self._data.get('suite_include')

    @suites_include.setter
    def suites_include(self, arg):
        self._data['suites_include'] = arg


class SuitesIds:
    @property
    def suites_ids(self):
        return self._data.get('suite_ids')

    @suites_ids.setter
    def suites_ids(self, arg):
        self._data['suites_ids'] = arg


class SectionsInclude:
    @property
    def sections_include(self):
        return self._data.get('sections_include')

    @sections_include.setter
    def sections_include(self, arg):
        self._data['sections_include'] = arg


class SectionsIds:
    @property
    def sections_ids(self):
        return self._data.get('sections_ids')

    @sections_ids.setter
    def sections_ids(self, arg):
        self._data['sections_ids'] = arg


class SystemNameMixin:
    @property
    def system_name(self):
        return self._data.get('name')

    @system_name.setter
    def system_name(self, arg):
        self._data['name'] = arg


class TemplateIdMixin:
    @property
    def template_id(self):
        return self._data.get('template_id')

    @template_id.setter
    def template_id(self, arg):
        self._data['title'] = int(arg)


class TestIdMixin:
    @property
    def test_id(self):
        return self._data.get('test_id')


class TitleMixin:
    @property
    def title(self):
        return self._data.get('title')

    @title.setter
    def title(self, arg):
        self._data['title'] = str(arg)


class TypeIdMixin:
    @property
    def type_id(self):
        return self._data.get('type_id')

    @type_id.setter
    def type_id(self, arg):
        self._data['type_id'] = int(arg)


class UntestedCountMixin:
    @property
    def untested_count(self):
        return self._data.get('untested_count')


class UpdatedByMixin:
    @property
    def updated_by(self):
        return self._data.get('updated_by')


class UpdatedOnMixin:
    @property
    def updated_on(self):
        return self._data.get('updated_on')


class UrlMixin:
    @property
    def url(self):
        return self._data.get('url')


class VersionMixin:
    @property
    def version(self):
        return self._data.get('version')

    @version.setter
    def version(self, arg):
        self._data['version'] = str(arg)
