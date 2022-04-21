from user import views
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

# * Viewsets routing parameters, kept on code for informational purposes

# api_router = routers.DefaultRouter()
# api_router.register(r"users", views.UserViewSet)
# api_router.register(r"profiles", views.ProfileViewSet)
# urlpatterns = [
#   path("", include(api_router.urls)),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.status),
    path('api/', views.status),
    path('api/profiles/', views.list_profiles, name="profiles"),
    path('api/profiles/<int:id>', views.profile_detail, name="profile"),
    path('api/users/', views.list_users, name="users"),
    path('api/users/<int:id>', views.user_detail, name="user"),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
