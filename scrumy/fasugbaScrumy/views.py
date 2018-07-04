from django.db import models
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import ScrumyUser, ScrumyGoals, ScrumyStatus, ScrumyUserJS, ScrumyGoalsJS, ScrumyStatusJS
from .forms import ScrumyUserForm, ScrumyGoalsForm, ScrumyStatusForm
from django.contrib.auth.models import Group, Permission,User
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets
from .serializers import ScrumyStatusSerializer, ScrumyUserSerializer, ScrumyGoalsSerializer, ScrumyStatusJSSerializer, ScrumyUserJSSerializer, ScrumyGoalsJSSerializer






# Create your views here.

def index1(request):
	size = ScrumyUser.objects.all()
	size = size.count()
	var = ScrumyUser.objects.filter(id__range=(1,size))
	var3 = ScrumyUser.objects.get(id=4)
	try:
		var2 = ScrumyUser.objects.get(id=4)

	except ObjectDoesNotExist as e:
		return HttpResponse("The id no do not exist in database")

	else:
			context ={
			'var': var,
			'var2': var2,
			'var3': var3,
			'size': size
			}	
			return render(request, 'fasugbaScrumy/index.html', context)


def index(request):
	user = request.user
	get_user = ScrumyUser.objects.get(username=user)
	userGoals = get_user.scrumygoals_set.filter(scrumy_user=get_user.id)
	context ={
			'user': user,
			'userGoals': userGoals			
			}	
	return render(request, 'fasugbaScrumy/index.html', context)
			




def add_task(request):
	user = request.user
	if request.method == 'POST':
		form = ScrumyGoalsForm(request.POST)

		if form.is_valid():
			get_user = ScrumyUser.objects.get(username=user)
			get_Status = ScrumyStatus.objects.get(pk=get_user.scrumy_user_role) 

			addTask = ScrumyGoals.objects.create(
				goals = form.cleaned_data.get('goals'),
				scrumy_status = get_Status, 
				scrumy_user = get_user
				)
			return redirect(index)

	else:
		form = ScrumyGoalsForm()
		all_user = ScrumyUser.objects.all()
	context = {
		'form': form,
		'user': user,
		'all_user': all_user
	}		
	return render(request, 'fasugbaScrumy/add_task.html', context)


def add_user(request):
	if request.method == 'POST':
		form = ScrumyUserForm(request.POST)
	
		if form.is_valid():
			user = User.objects.create_user('form.first_name', 'form.email', 'form.password')
			addUser = form.save(commit=False)
			addUser.save()
			return redirect('index')

	else:			
		form = ScrumyUserForm()
		context = {
		'form': form
	}	
	return render(request, 'fasugbaScrumy/add_user.html', context)

def get_all_user(request):

	# get_users = ScrumyUser.objects.all()

	# add_group = get_users.groups.add_group(ADMIN)
 #    user = request.user    
 #    user.groups.add(different_users)   
 #    user.groups.add(outstanding_users)

	# user = User.objects.create_user('fashola', 'Fashola@yahoo.com', 'Ayomi1234')
	# user.first_name = 'Fashola'
	# user.last_name = 'Ayodeji'
	# user.save()
	# # all_users = ScrumyUser.objects.all()

	# # for each_user in all_users:
	# # 	each_user.scrumy_user_role = 1
	# # 	each_user.save
	# changed_users = ScrumyUser.objects.all() 
	# context = {
	#  	'changed_users': changed_users,
	#  }		
	return render(request, 'fasugbaScrumy/users.html', context)
	
		
	


		

		



def move_task(request):
	user = request.user
	get_user = ScrumyUser.objects.get(username=user)
	get_Status = ScrumyStatus.objects.all() 
	#getTask = ScrumyGoals.objects.get(pk = task_id)
	if request.method == 'POST':
		form = ScrumyGoalsForm(request.POST)
		
		new_goal = request.POST['goal']

		if user.has_perm("fasugbaScrumy.WG_to_DT") and ScrumyStatus.objects.get(pk=1) == ScrumyGoals.objects.get(goals = request.POST['goal']).scrumy_status:
			move_task = ScrumyGoals.objects.get(goals = request.POST['goal'])
			move_task.scrumy_status = ScrumyStatus.objects.get(pk=2)
			move_task.save()	
		elif user.has_perm("fasugbaScrumy.DT_to_verify") and ScrumyStatus.objects.get(pk=2) == ScrumyGoals.objects.get(goals = request.POST['goal']).scrumy_status:
			move_task = ScrumyGoals.objects.get(goals = request.POST['goal'])
			move_task.scrumy_status = ScrumyStatus.objects.get(pk=3)
			move_task.save()
		elif user.has_perm("fasugbaScrumy.verify_t0_done") and ScrumyStatus.objects.get(pk=3) == ScrumyGoals.objects.get(goals = request.POST['goal']).scrumy_status:
			move_task = ScrumyGoals.objects.get(goals = request.POST['goal'])
			move_task.scrumy_status = ScrumyStatus.objects.get(pk=4)
			move_task.save()
		elif user.has_perm("fasugbaScrumy.anywhere_to_anywhere"):
			new_status = request.POST['new_status']
			move_task = ScrumyGoals.objects.get(goals = request.POST['goal'])
			move_task.scrumy_status = ScrumyStatus.objects.get(name=new_status)
			move_task.save()
		else:
			return HttpResponse("You do not have Permissionto move this task")

		users_object = ScrumyUser.objects.all()
		context = {
			'users_object': users_object
		}
		return render(request, 'fasugbaScrumy/goals_view.html', context)
	else:
		#form = ScrumyGoalsForm()

		# all_status = ScrumyStatus.objects.all()
		# all_goals = ScrumyGoals.objects.all()
		# weekly_goals = ScrumyGoals.objects.filter(scrumy_user=get_user.id)
		# daily_goals = ScrumyGoals.objects.filter(scrumy_user=get_user.id)
		# verify = ScrumyGoals.objects.filter(scrumy_user=get_user.id)

		all_status = ScrumyStatus.objects.all()
		all_goals = ScrumyGoals.objects.all()		
		weekly_goals = ScrumyGoals.objects.filter(scrumy_user=get_user.id)
		daily_goals = ScrumyGoals.objects.filter(scrumy_status=2)
		verify = ScrumyGoals.objects.filter(scrumy_status=3)
		context = {
			#'form': form,
			#'getTask': getTask,
			#'task': task,
			'all_goals': all_goals,
			'all_status': all_status,
			'weekly_goals': weekly_goals,
			'daily_goals': daily_goals,
			'verify': verify


		}	
	return render(request, 'fasugbaScrumy/move_task.html', context)




class goals_view(generic.ListView):

    template_name = 'fasugbaScrumy/goals_view.html'

    context_object_name = 'users_object'

    def get_queryset(self):

        return ScrumyUser.objects.all()


def signup(request):
    firstname=''
    lastname=''
    emailvalue=''
    uservalue=''
    passwordvalue1=''
    passwordvalue2=''

    form= ScrumyUserForm(request.POST or None)
    if form.is_valid():
        fs= form.save(commit=False)
        firstname= form.cleaned_data.get("first_name")
        lastname= form.cleaned_data.get("last_name")
        emailvalue= form.cleaned_data.get("email")
        uservalue= form.cleaned_data.get("username")
        passwordvalue1= form.cleaned_data.get("password1")
        passwordvalue2= form.cleaned_data.get("password2")
        scrumy_user_role = form.cleaned_data.get("scrumy_user_role")

        if passwordvalue1 == passwordvalue2:
            try:
                user= User.objects.get(username=uservalue) #if able to get, user exists and must try another username
                context= {'form': form, 'error':'The username you entered has already been taken. Please try another username.'}
                return render(request, 'fasugbaScrumy/signup.html', context)
            except User.DoesNotExist:
            	user= User.objects.create_user(uservalue, password= passwordvalue1,email=emailvalue, is_staff= True)
            	user.first_name = firstname
            	user.last_name = lastname
            	if scrumy_user_role == 1: #Developer
            		#user.user_permissions.add(28)#WG-DT
	            	user.groups.add(1)
            	elif scrumy_user_role == 2: #Admin
            		#user.user_permissions.add(26)# DT-VERIFY
            		user.groups.add(2)
            	elif scrumy_user_role == 3:#QA
            		#user.user_permissions.add(27)#VERIFY-DONE
            		user.groups.add(3)
            	elif scrumy_user_role == 4:#Owner
            		#user.user_permissions.add(25)#ANYWHERE
            		user.groups.add(4)
            	else:
	            	return HttpResponse()

            	
            	user.save()

            	login(request,user)

            	fs.user= request.user

            	fs.save()
            	context= {'form': form}
            	return render(request, 'fasugbaScrumy/index.html', context)
            
        else:
            context= {'form': form, 'error':'The passwords that you provided don\'t match'}
            return render(request, 'fasugbaScrumy/signup.html', context)
        

    else:
        context= {'form': form}
        return render(request, 'fasugbaScrumy/signup.html', context)


class ScrumyUserViewSet(viewsets.ModelViewSet):
    queryset = ScrumyUser.objects.all()
    serializer_class = ScrumyUserSerializer

    # @detail_route()
    def scrumygoals(self, request, pk=None):
        scrumyuser = self.get_object()
        serializer = ScrumyGoalsSerializer(scrumyuser.comments.all(), context={'request': request}, many=True)
        return Response(serializer.data)


class ScrumyStatusViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = ScrumyStatusSerializer

	def scrumystatus(self, request, pk=None):
		scrumystatus = self.get_object()
		serializer = ScrumyGoalsSerializer(scrumystatus.comments.all(), context={'request': request}, many=True)
		return Response(serializer.data)


class ScrumyGoalsViewSet(viewsets.ModelViewSet):
    queryset = ScrumyGoals.objects.all()
    serializer_class = ScrumyGoalsSerializer




####################################################################




class ScrumyUserJSViewSet(viewsets.ModelViewSet):
    queryset = ScrumyUserJS.objects.all()
    serializer_class = ScrumyUserJSSerializer

    def scrumygoals(self, request, pk=None):
        scrumyuserjs = self.get_object()
        serializer = ScrumyGoalsJSSerializer(scrumyuserjs.comments.all(), context={'request': request}, many=True)
        return Response(serializer.data)


class ScrumyStatusJSViewSet(viewsets.ModelViewSet):
	queryset = ScrumyStatusJS.objects.all()
	serializer_class = ScrumyStatusJSSerializer

	# def scrumystatus(self, request, pk=None):
	# 	scrumystatusjs = self.get_object()
	# 	serializer = ScrumyGoalsJSSerializer(scrumystatusjs.comments.all(), context={'request': request}, many=True)
	# 	return Response(serializer.data)


class ScrumyGoalsJSViewSet(viewsets.ModelViewSet):
    serializer_class = ScrumyGoalsJSSerializer

    def get_queryset(self):
    	queryset = ScrumyGoalsJS.objects.all()
    	return queryset



def Scrumy_app(request):
	user = request.user
	context_dict = {
			'user': user		
			}	
	return render_to_response('fasugbaScrumy/scrumy.html', context_dict, RequestContext(request))
    # """
    # List all code snippets, or create a new snippet.
    # """
    # if request.method == 'GET':
    #     snippets = Snippet.objects.all()
    #     serializer = SnippetSerializer(snippets, many=True)
    #     return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


