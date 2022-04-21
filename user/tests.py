import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .api.serializers import ProfileSerializer, UserSerializer
from .models import CustomUser as User
from .models import Profile


# User creation class method
class UserAPITestCase(APITestCase):

    def create_user(self):
        data = {"username" : "lorem", "password" : 'ipsum', 
                    "email" : "loremipsum@email.com"}
        response = self.client.post(reverse('users'), data)
        return response

# All user endpoint tests section
class UserListTestCase(UserAPITestCase):

    def test_creation(self):
        response = self.create_user()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["username"], "lorem")
        self.assertEqual(response.data["password"], "ipsum")
        self.assertEqual(response.data["email"], "loremipsum@email.com")


    def test_retrieve_all(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data["users"], list)

    
    def test_retrieve_one(self):
        response = self.create_user()
        res = self.client.get(reverse("user", kwargs={'id': response.data['id']}))
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        todo = User.objects.get(id=response.data['id'])
        self.assertEqual(todo.username, res.data['username'])


    def test_update_one(self):
        
        response = self.create_user()
        res = self.client.put(reverse("user", kwargs={'id': response.data['id']}), {
            "username" : "newusername",
            "password" : "newpassword",
            "email" : "loremipsum@email.com"
        })
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        updated_user = User.objects.get(id=response.data['id'])
        self.assertEqual(updated_user.username, "newusername")


    def test_delete_one(self):
        response = self.create_user()
        previous_db_count = User.objects.all().count()

        self.assertGreater(previous_db_count, 0)
        self.assertEqual(previous_db_count, 1)

        res = self.client.delete(reverse("user", kwargs={'id': response.data['id']}))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(User.objects.all().count(), 0)


# Profile creation class method
class ProfileAPITestCase(UserAPITestCase):

    def create_profile(self):
        user_response = self.create_user()
        data = {"name": "test_profile_name",
                    "last_name": "test_profile_last_name",
                    "birth_date": "2022-04-21",
                    "related_user": user_response.data['id']}
        response = self.client.post(reverse('profiles'), data)
        return response


# All profile endpoint tests
class ProfileListTestCase(ProfileAPITestCase):

    def test_creation(self):
        response = self.create_profile()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "test_profile_name")
        self.assertEqual(response.data["last_name"], "test_profile_last_name")
        self.assertEqual(response.data["birth_date"], "2022-04-21")
        self.assertEqual(response.data["related_user"], 1)

    
    def test_retrieve_all(self):
        response = self.client.get(reverse('profiles'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data["profiles"], list)

    
    def test_retrieve_one(self):
        response = self.create_profile()
        res = self.client.get(reverse("user", kwargs={'id': response.data['id']}))
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        todo = User.objects.get(id=response.data['id'])
        self.assertEqual(todo.username, res.data['username'])


    def test_update_one(self):
        
        response = self.create_profile()
        res = self.client.put(reverse("profile", kwargs={'id': response.data['id']}), {
            "name": "new_test_profile_name",
            "last_name": "new_test_profile_last_name",
            "birth_date": "2022-04-21",
            "related_user": response.data['related_user']
        })
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        updated_profile = Profile.objects.get(id=response.data['id'])
        self.assertEqual(updated_profile.name, "new_test_profile_name")


    def test_delete_one(self):
        response = self.create_profile()
        previous_db_count = Profile.objects.all().count()

        self.assertGreater(previous_db_count, 0)
        self.assertEqual(previous_db_count, 1)

        res = self.client.delete(reverse("profile", kwargs={'id': response.data['id']}))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Profile.objects.all().count(), 0)


    