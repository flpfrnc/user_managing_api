from django.contrib import admin
from .models import Profile, CustomUser as User

admin.site.register(Profile)
admin.site.register(User)