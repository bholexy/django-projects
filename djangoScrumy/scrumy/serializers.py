# scrumy/serializers.py
from rest_framework import serializers
# from . import models
from .models import CustomUser, ScrumyGoals, ScrumyStatus, ScrumyStory
import time


class ScrumyGoalsSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	goals = serializers.CharField(required=True, allow_blank=False, max_length=100)	
	scrumy_user_id = serializers.CharField(style={'base_template': 'textarea.html'})
	scrumy_status_id = serializers.CharField(style={'base_template': 'textarea.html'})

	class Meta:
		model = ScrumyGoals
		fields = ('id', 'goals', 'scrumy_user_id', 'scrumy_status_id')

	# def get_permissions(self, instance, validated_data, request):
	# 	if request.method in SAFE_METHOD:
	# 		pass
	# 	else:
	# 		if (IsDeveloper):
	# 			if scrumy_status_id == 1 or scrumy_status_id == 2:
	# 				instance.goals = self.validated_data['goals']
	# 				instance.scrumy_user_id = self.validated_data['scrumy_user_id']
	# 				instance.scrumy_status_id = self.validated_data['scrumy_status_id']
	# 				instance.save()
	# 				return instance

	# 		elif (IsAdmin):
	# 			if scrumy_status_id == 2 or scrumy_status_id == 3:
	# 				instance.goals = self.validated_data['goals']
	# 				instance.scrumy_user_id = self.validated_data['scrumy_user_id']
	# 				instance.scrumy_status_id = self.validated_data['scrumy_status_id']
	# 				instance.save()
	# 				return instance

	# 		elif (IsQA):
	# 			if scrumy_status_id == 3 or scrumy_status_id == 4:
	# 				instance.goals = self.validated_data['goals']
	# 				instance.scrumy_user_id = self.validated_data['scrumy_user_id']
	# 				instance.scrumy_status_id = self.validated_data['scrumy_status_id']
	# 				instance.save()
	# 				return instance

	# 		elif (IsOwner):
	# 			if scrumy_status_id == range(1,4):
	# 				instance.goals = self.validated_data['goals']
	# 				instance.scrumy_user_id = self.validated_data['scrumy_user_id']
	# 				instance.scrumy_status_id = self.validated_data['scrumy_status_id']
	# 				instance.save()
	# 				return instance


	# 		else:
	# 			message = 'You do not have permission'
	# 			return message
	# 	return False
   


class ScrumyStatusSerializer(serializers.HyperlinkedModelSerializer):
	name = serializers.CharField(required=True, allow_blank=False, max_length=100)
	scrumygoals = ScrumyGoalsSerializer(many=True, read_only=True)
	url = serializers.HyperlinkedIdentityField(view_name = 'status-detail')
	
	class Meta:
		fields = ('url','id', 'name', 'scrumygoals')
		model = ScrumyStatus


class ScrumyStorySerializer(serializers.HyperlinkedModelSerializer):
	story = serializers.CharField(required=True, allow_blank=False, max_length=100)
	scrumygoals = ScrumyGoalsSerializer(many=True, read_only=True)
	url = serializers.HyperlinkedIdentityField(view_name = 'story-detail')

	class Meta:
		fields = ('url', 'id', 'story','scrumygoals')
		model = ScrumyStory



class UserSerializer(serializers.ModelSerializer):
	scrumy_goals = ScrumyGoalsSerializer(many=True, read_only=True)

	class Meta:
		model = CustomUser
		fields = ('__all__')




class ScrumyGoalsPostSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	goals = serializers.CharField(required=True, allow_blank=False, max_length=100)	
	scrumy_user_id = serializers.CharField(style={'base_template': 'textarea.html'})
	scrumy_status_id = serializers.CharField(style={'base_template': 'textarea.html'})

	class Meta:
		model = ScrumyGoals
		fields = ('id', 'goals', 'scrumy_user_id', 'scrumy_status_id')



# class GoalListingField(serializers.RelatedField):
#     def to_representation(self, value):
#         return ' %d: %s (%s)' % (value.goals, value.scrumy_status_id, value.scrumy_user_id)



# class UserSerializer(serializers.ModelSerializer):
# 	# scrumygoals = ScrumyGoalsSerializer(many=True, read_only=True)
# 	scrumygoals = ScrumyGoalsSerializer(many=True, read_only=True)

# 	class Meta:
# 		model = CustomUser
# 		fields = ('id', 'email', 'username', 'scrumygoals')
