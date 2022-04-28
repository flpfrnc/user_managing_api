from rest_framework import serializers
from ..models import Profile, CustomUser as User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    related_user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'