import logging
from schema import Schema, Or

from testrail.models.base import PostModel

from testrail.models.mixins.fields.assignedto_id import AssignedToIdMixin
from testrail.models.mixins.fields.comment import CommentMixin
from testrail.models.mixins.fields.created_by import CreatedByMixin
from testrail.models.mixins.fields.created_on import CreatedOnMixin
from testrail.models.mixins.fields.defects import DefectsMixin
from testrail.models.mixins.fields.elapsed import ElapsedMixin
from testrail.models.mixins.fields.id import IdMixin
from testrail.models.mixins.fields.status_id import StatusIdMixin
from testrail.models.mixins.fields.test_id import TestIdMixin
from testrail.models.mixins.fields.version import VersionMixin

from testrail.models.mixins.methods.add import AddMixin


class ResultModel(AssignedToIdMixin, CommentMixin, CreatedByMixin, CreatedOnMixin, DefectsMixin, ElapsedMixin, IdMixin,
                  StatusIdMixin, TestIdMixin, VersionMixin, AddMixin, PostModel):

    ENDPOINTS = {
        'add': 'add_result/{test_id}}',
        'add_collection': 'add_results/{run_id}'
    }

    POST_FIELDS = {
        'add': [
            'status_id',
            'comment',
            'version',
            'elapsed',
            'defects',
            'suite_mode',
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
        'version': Or(str, None)
    })

    def add(self, test_id=None):
        if self.test_id:
            test_id = self.test_id
        if self.test_id and test_id:
            logging.warning(msg='Instance variable of `test id` takes precedence over `test id` kwarg.')

        response = self._add(test_id=test_id)
        self._update_data(response)
