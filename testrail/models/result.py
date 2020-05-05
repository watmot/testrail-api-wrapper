from schema import Schema, Or

from testrail.models.base import PostModel

from testrail.models.mixins.fields import AssignedToIdMixin
from testrail.models.mixins.fields import CommentMixin
from testrail.models.mixins.fields import CreatedByMixin
from testrail.models.mixins.fields import CreatedOnMixin
from testrail.models.mixins.fields import DefectsMixin
from testrail.models.mixins.fields import ElapsedMixin
from testrail.models.mixins.fields import IdMixin
from testrail.models.mixins.fields import StatusIdMixin
from testrail.models.mixins.fields import TestIdMixin
from testrail.models.mixins.fields import VersionMixin

from testrail.models.mixins.methods import AddMixin


class ResultModel(AssignedToIdMixin, CommentMixin, CreatedByMixin, CreatedOnMixin, DefectsMixin, ElapsedMixin, IdMixin,
                  StatusIdMixin, TestIdMixin, VersionMixin, AddMixin, PostModel):

    ENDPOINTS = {
        'add': 'add_result/{test_id}'
    }

    POST_FIELDS = {
        'add': [
            'status_id',
            'comment',
            'version',
            'elapsed',
            'defects',
            'assigned_to_id'
        ]
    }

    SCHEMA = Schema({
        'assignedto_id': Or(int, None),
        'comment': Or(str, None),
        'created_by': int,
        'created_on': int,
        'custom_step_results': Or(list, None),
        'defects': Or(str, None),
        'elapsed': Or(str, None),
        'id': int,
        'status_id': int,
        'test_id': int,
        'version': Or(str, None),

    },
        ignore_extra_keys=True
    )

    def add(self, test_id):
        response = self._add(test_id=test_id)
        return response
