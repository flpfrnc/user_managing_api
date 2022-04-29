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

    def to_representation(self, instance):
       ret = super().to_representation(instance)
       ret['related_user'] = UserSerializer(instance.related_user).data
       return ret
