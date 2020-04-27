class ProjectIdMixin:
    @property
    def project_id(self):
        return self._data.get('project_id')

    @project_id.setter
    def project_id(self, arg):
        self._data['project_id'] = arg

    # TODO add something in to make sure properties can only be updated under certain circumstances
