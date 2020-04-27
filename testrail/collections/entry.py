from testrail.collections.base import BaseCollection
from testrail.models.entry import EntryModel


class EntryCollection(BaseCollection):
    MODEL = EntryModel
