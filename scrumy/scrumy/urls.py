"""myscrumy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include,re_path
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from fasugbaScrumy.views import ScrumyUserViewSet, ScrumyStatusViewSet, ScrumyGoalsViewSet, ScrumyUserJSViewSet, ScrumyStatusJSViewSet, ScrumyGoalsJSViewSet


router = DefaultRouter()

router.register(prefix = 'users', viewset = ScrumyUserViewSet, base_name = "MyUser")
router.register(prefix = 'goals', viewset = ScrumyGoalsViewSet, base_name = "MyGoals")
router.register(prefix = 'status', viewset = ScrumyStatusViewSet, base_name = "MyStatus")
router.register(prefix = 'usersjs', viewset = ScrumyUserJSViewSet,  base_name = "usersjs")
router.register(prefix = 'goalsjs', viewset = ScrumyGoalsJSViewSet, base_name = "goalsjs")
router.register(prefix = 'statusjs', viewset = ScrumyStatusJSViewSet,  base_name = "statusjs")



urlpatterns = [
    url(r'^', include('fasugbaScrumy.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^fasugbaScrumy/', include('fasugbaScrumy.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^login/$', auth_views.login),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]


urlpatterns += router.urls
