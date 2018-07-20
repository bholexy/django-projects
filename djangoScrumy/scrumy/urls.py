# scrumy/urls.py
from django.urls import include, path
from . import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('users', views.UserListView.as_view()),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('auth/', ObtainAuthToken.as_view()),
]


