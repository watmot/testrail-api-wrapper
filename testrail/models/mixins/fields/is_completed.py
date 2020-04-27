class IsCompletedMixin:
    @property
    def is_completed(self):
        return self._data.get('is_completed')

    @is_completed.setter
    def is_completed(self, arg):
        self._data['is_completed'] = True if bool(arg) else False





# self._post_fields




# model.is_completed  => True
# model.