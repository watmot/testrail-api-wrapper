import random

from testrail import Testrail
from testrail.models.user import UserModel


class TestSuite:
    def test_get_users(self):
        users = Testrail.users()
        index = random.randint(0, len(users)-1)

        assert isinstance(users[index], UserModel)

    def test_get_user(self):
        users = Testrail.users()
        index = random.randint(0, len(users) - 1)

        user = Testrail.user(user_id=users[index].id)

        assert isinstance(user, UserModel)