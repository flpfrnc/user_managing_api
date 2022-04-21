from django.http import JsonResponse
from .models import *
from .api.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *


from rest_framework import viewsets
from .models import CustomUser as User, Profile

# * Viewsets could have been used to simplify the implementation
# * it was kept on code for informational purposes 

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer


@api_view(['GET'])
def status(request):
    """check either the base endpoint is accessible or not"""
    return Response({ "status" : "online"},  status=HTTP_200_OK)


# profile function based view
@api_view(['GET', 'POST'])
def list_profiles(request, format=None):
    """Lists and inserts profiles into DB"""
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response({ "profiles" :  serializer.data}, status=HTTP_200_OK)

    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def profile_detail(request, id, format=None):
    """Details an specific profile receiving it's id, also permitting alteration and deletion"""

    # error handlers on finding the object
    try:
        profile = Profile.objects.get(pk=id)
    except Profile.DoesNotExist:
        return Response({"profiles": "profile not found"}, status=HTTP_404_NOT_FOUND)

    # method division
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        profile.delete()
        return Response({"profiles": f"profile {id} deleted"}, status=HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def list_users(request, format=None):
    """Lists and inserts users into DB"""
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({ "users" :  serializer.data}, status=HTTP_200_OK)

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def user_detail(request, id, format=None):
    """Details an specific user receiving it's id, also permitting alteration and deletion"""

    # error handlers on finding the object
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response({"users": "user not found"}, status=HTTP_404_NOT_FOUND)

    # method division
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response({"users": f"user {id} deleted"}, status=HTTP_204_NO_CONTENT)