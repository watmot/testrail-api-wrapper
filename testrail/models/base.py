import json


class BaseModel:
    ENDPOINTS = None
    SCHEMA = None

    def __init__(self, data=None):
        self._data = {}

        if data:
            self._update_data(data)

    def _update_data(self, data):
        validated_data = self.SCHEMA.validate(data)
        self._data.update(validated_data)


class PostModel(BaseModel):
    POST_FIELDS = None

    def _filter_post_data(self, method):
        post_data = json.dumps({k: v for k, v in self._data.items() if k in self.POST_FIELDS[method]})

        return post_data
