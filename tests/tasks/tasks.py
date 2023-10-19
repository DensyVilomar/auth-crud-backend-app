import pytest
from apps.tasks.models import Task
from apps.users.models import UserAccount


@pytest.mark.django_db
def test_task_creation():

    user = UserAccount(id="6db6e472-cc5f-40d4-b89b-c2779f69f732")

    task = Task.objects.create(
        title="one",
        deadline="2023-11-22",
        creator=user
    )
