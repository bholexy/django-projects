from . import views 
from django.conf.urls import url
from django.contrib.auth.decorators import login_required,permission_required,user_passes_test



urlpatterns = [
    url(r'^$', login_required(views.index), name = 'index'),
    url(r'^movetask$', login_required(views.move_task), name = 'move_goal'),
     url(r'^adduser$', login_required(views.add_user), name = 'add_user'),
     url(r'^addtask$', login_required(views.add_task), name = 'add_task'),
     url(r'^userss$', views.get_all_user, name = 'userss'),     
    url(r'^signup/$', views.signup,  name = 'signup'),
     url('view_goal/', views.goals_view.as_view(), name='view_goals'),

      url(r'^scrumy$', views.Scrumy_app, name = 'Scrumy'),

   ]