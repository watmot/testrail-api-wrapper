from schema import Schema, Or, Regex, Optional

from testrail.models.base import PostModel
from testrail.models.mixins.fields import (AssignedToIdMixin, CommentMixin, CreatedByMixin, CreatedOnMixin,
                                           DefectsMixin, ElapsedMixin, IdMixin, StatusIdMixin, TestIdMixin,
                                           VersionMixin)
from testrail.models.mixins.methods import AddMixin


class ResultModel(AssignedToIdMixin, CommentMixin, CreatedByMixin, CreatedOnMixin, DefectsMixin, ElapsedMixin, IdMixin,
                  StatusIdMixin, TestIdMixin, VersionMixin, AddMixin, PostModel):

    ENDPOINTS = {
        'add': 'add_result/{test_id}',
        'add_case': 'add_result_for_case/{run_id}/{case_id}'
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
        'defects': Or(str, None),
        'elapsed': Or(str, None),
        'id': int,
        'status_id': int,
        'test_id': int,
        'version': Or(str, None),
        Optional(Regex(r'^custom_')): object
    })

    def add(self, test_id):
        response = self._add(test_id=test_id)
        return response

    def add_for_case(self, run_id, case_id):
        response = self._add(field='case', run_id=run_id, case_id=case_id)
        return response
