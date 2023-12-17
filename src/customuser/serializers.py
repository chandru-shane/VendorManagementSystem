import re

from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers


User = get_user_model()

regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"


def is_email(email):
    """This function returns True if given argument is email
    else returns False"""

    if re.search(regex, email):
        return True
    else:
        return False


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True, "min_length": 8}}

    def create(self, validated_data):
        """Create new user with encrypted password and return it"""
        User = get_user_model()
        created_user = User.objects.create_user(**validated_data)
        return created_user
