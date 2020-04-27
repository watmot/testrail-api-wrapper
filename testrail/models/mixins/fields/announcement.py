class AnnouncementMixin:
    @property
    def announcement(self):
        return self._data.get('announcement')

    @announcement.setter
    def announcement(self, arg):
        self._data['announcement'] = str(arg)