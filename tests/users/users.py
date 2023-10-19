import pytest
from datetime import datetime
from apps.users.models import UserAccount


@pytest.mark.django_db
def test_user_creation():
    user = UserAccount.objects.create(
        email="n@gmail.com",
        username="n123",
        first_name="n",
        last_name="nn",
        date_of_birth=datetime.strptime("2000-12-12", "%Y-%m-%d")

    )
