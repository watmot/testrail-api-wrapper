class PlanIdMixin:
    @property
    def plan_id(self):
        return self._data.get('plan_id')

    @plan_id.setter
    def plan_id(self, arg):
        self._data['plan_id'] = int(arg)

    # TODO add something in to make sure properties can only be updated under certain circumstances
