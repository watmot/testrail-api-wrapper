class CommentMixin:
    @property
    def comment(self):
        return self._data.get('comment')

    @comment.setter
    def comment(self, arg):
        self._data['comment'] = str(arg)
