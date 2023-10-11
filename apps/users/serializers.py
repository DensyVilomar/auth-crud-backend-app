from djoser.serializers import UserCreateSerializer
from .models import UserAccount


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = UserAccount
        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'age',
        ]
