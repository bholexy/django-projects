

# users/views.py
from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets

# from .permissions import IsDeveloper, IsAdmin, IsQA, IsOwner
from .serializers import UserSerializer, ScrumyStorySerializer, ScrumyStatusSerializer, ScrumyGoalsSerializer

from .models import CustomUser, ScrumyGoals, ScrumyStatus, ScrumyStory

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
# from . import models


User = get_user_model()



# class UserListView(generics.ListCreateAPIView):
# 	queryset = CustomUser.objects.all()
# 	serializer_class = UserSerializer
# 	# authentication_classes = (TokenAuthentication,)
# 	# permission_classes = (IsAuthenticated,)


# 	def create( self, request, *args, **kwargs):
# 		serializer = self.get_serializer(data=request.data)
# 		serializer.is_valid(raise_exception = True )
# 		self.perform_create(serializer)
# 		headers = self.get_success_headers(serializer.data)
# 		token,created = Token.objects.get_or_create(user=serializer.instance)
# 		return Response ({ 
# 			'token' : token.key, 
# 			'id' :serializer.instance.id},
# 		status=status.HTTP_201_CREATED,headers=headers)


class UserListView(generics.ListCreateAPIView):
	queryset = CustomUser.objects.all()
	serializer_class = UserSerializer
	# authentication_classes = (TokenAuthentication,)
	# permission_classes = (IsAuthenticated,)


	# def create( self, request, *args, **kwargs):
	# 	serializer = self.get_serializer(data=request.data)
	# 	serializer.is_valid(raise_exception = True )
	# 	self.perform_create(serializer)
	# 	headers = self.get_success_headers(serializer.data)
	# 	token,created = Token.objects.get_or_create(user=serializer.instance)
	# 	return Response ({ 
	# 		'token' : token.key, 
	# 		'id' :serializer.instance.id},
	# 	status=status.HTTP_201_CREATED,headers=headers)



class ScrumyStoryViewSet(viewsets.ModelViewSet):
    queryset = ScrumyStory.objects.all()
    serializer_class = ScrumyStorySerializer

    def scrumygoals(self, request, pk=None):
        scrumystory = self.get_object()
        serializer = ScrumyGoalsJSSerializer(scrumystory.comments.all(), context={'request': request}, many=True)
        return Response(serializer.data)


class ScrumyStatusViewSet(viewsets.ModelViewSet):
	queryset = ScrumyStatus.objects.all()
	serializer_class = ScrumyStatusSerializer


class ScrumyGoalsViewSet(viewsets.ModelViewSet):
	queryset = ScrumyGoals.objects.all()
	serializer_class = ScrumyGoalsSerializer

	