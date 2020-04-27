class ShowAnnouncementMixin:
    @property
    def show_announcement(self):
        return self._data.get('show_announcement')

    @show_announcement.setter
    def show_announcement(self, arg):
        self._data['show_announcement'] = True if bool(arg) else False
