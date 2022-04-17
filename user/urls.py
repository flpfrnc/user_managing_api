from user import views
from django.contrib import admin
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/', views.list_profiles),
    path('profiles/<int:id>', views.profile_detail),
    path('users/', views.list_users),
    path('users/<int:id>', views.user_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])