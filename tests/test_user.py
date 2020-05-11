import random

from testrail import Testrail
from testrail.models.user import UserModel


class TestSuite:
    def test_get_users(self):
        users = Testrail.users()
        users.get()
        index = random.randint(0, len(users)-1)

        assert isinstance(users[index], UserModel)

    def test_get_user_by_id(self):
        users = Testrail.users()
        users.get()
        index = random.randint(0, len(users) - 1)

        user = Testrail.user()
        user.get(user_id=users[index].id)

        assert isinstance(user, UserModel)

    def test_get_user_by_email(self):
        users = Testrail.users()
        users.get()
        index = random.randint(0, len(users) - 1)
            
        user = Testrail.user()
        user.get_by_email(email=users[index].email)

        assert isinstance(user, UserModel)
