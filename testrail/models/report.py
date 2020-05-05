from schema import Schema, Optional, Or

from testrail.models.base import BaseModel

from testrail.models.mixins.fields import (IdMixin, NameMixin, DescriptionMixin, NotifyUserMixin, NotifyLinkMixin,
                                           NotifyLinkRecipientsMixin, NotifyAttachmentMixin,
                                           NotifyAttachmentHTMLFormatMixin, NotifyAttachmentPDFFormatMixin,
                                           CasesGroupByMixin, ChangesDateRangeMixin, ChangesDateRangeFromMixin,
                                           ChangesDateRangeToMixin, SuitesInclude, SuitesIds, SectionsInclude,
                                           SectionsIds, CasesColumnsMixin, CasesFiltersMixin, CasesLimitMixin,
                                           ContentHideLinksMixin, CasesIncludeNewMixin, CasesIncludeUpdatedMixin)


class ReportModel(IdMixin, NameMixin, DescriptionMixin, NotifyUserMixin, NotifyLinkMixin, NotifyLinkRecipientsMixin,
                  NotifyAttachmentMixin, NotifyAttachmentHTMLFormatMixin, NotifyAttachmentPDFFormatMixin,
                  CasesGroupByMixin, ChangesDateRangeMixin, ChangesDateRangeFromMixin, ChangesDateRangeToMixin,
                  SuitesInclude, SuitesIds, SectionsInclude, SectionsIds, CasesColumnsMixin, CasesFiltersMixin,
                  CasesLimitMixin, ContentHideLinksMixin, CasesIncludeNewMixin, CasesIncludeUpdatedMixin, BaseModel):
    SCHEMA = Schema({
        'id': int,
        'name': str,
        'description': Or(str, None),
        'notify_user': bool,
        'notify_link': bool,
        'notify_link_recipients': str,
        'notify_attachment': bool,
        'notify_attachment_html_format': bool,
        'notify_attachment_pdf_format': bool,
        Optional('cases_groupby'): str,
        Optional('changes_daterange'): str,
        Optional('changes_daterange_from'): Or(str, None),
        Optional('changes_daterange_to'): Or(str, None),
        Optional('suites_include'): str,
        Optional('suites_ids'): Or(str, None),
        Optional('sections_include'): str,
        Optional('sections_ids'): Or(str, None),
        Optional('cases_columns'): dict,
        Optional('cases_filters'): Or(str, None),
        Optional('cases_limit'): int,
        Optional('content_hide_links'): bool,
        Optional('cases_include_new'): bool,
        Optional('cases_include_updated'): bool
    })
