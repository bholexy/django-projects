from rest_framework import serializers
from .models import ScrumyUser, ScrumyGoals, ScrumyStatus, ScrumyStatusJS, ScrumyUserJS, ScrumyGoalsJS



class ScrumyStatusSerializer(serializers.HyperlinkedModelSerializer):
	name = serializers.CharField(required=True, allow_blank=False, max_length=100)

	def create(self, validated_data):
	# """
	# Create and return a new `Snippet` instance, given the validated data.
	# """
		return ScrumyStatuss.objects.create(**validated_data)

	def update(self, instance, validated_data):
		 # """
        # Update and return an existing `Snippet` instance, given the validated data.
        # ""
		instance.name = validated_data.get('name', instance.name)
		instance.save()
		return instance

	class Meta:
		fields = ('id', 'name')
		model = ScrumyStatus



class ScrumyGoalsSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)
	goals = serializers.CharField(required=True, allow_blank=False, max_length=100)
	scrumy_user_id = serializers.CharField(style={'base_template': 'textarea.html'})
	scrumy_status_id = serializers.CharField(style={'base_template': 'textarea.html'})

	def create(self, validated_data):
	# """
	# Create and return a new `Snippet` instance, given the validated data.
	# """
		return ScrumyGoals.objects.create(**validated_data)

	def update(self, instance, validated_data):
		 # """
        # Update and return an existing `Snippet` instance, given the validated data.
        # ""
		instance.goals = validated_data.get('goals', instance.goals)
		instance.scrumy_user_id = validated_data.get('scrumy_user_id', instance.scrumy_user_id)
		instance.scrumy_status_id = validated_data.get('scrumy_status_id', instance.scrumy_status_id)
		instance.save()
		return instance

	class Meta:
		fields = ('id', 'goals', 'scrumy_user_id', 'scrumy_status_id')
		model = ScrumyGoals


class ScrumyUserSerializer(serializers.HyperlinkedModelSerializer):
	# scrumygoals_set = ScrumyGoalsSerializer(many=True, read_only=True)
	# scrumygoals = serializers.HyperlinkedIdentityField(view_name='scrumyuser-scrumygoals')
	scrumygoals = ScrumyGoalsSerializer(many=True, read_only=True)

	class Meta:
		fields = ('id', 'username', 'email', 'phone_no', 'gender','scrumygoals')
		model = ScrumyUser

















class ScrumyGoalsJSSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)
	goals = serializers.CharField(style={'base_template': 'textarea.html'})
	# url = serializers.PrimaryKeyRelatedField(read_only = True, many = True)
	# scrumy_user = serializers.HyperlinkedIdentityField(many = True, read_only = True, view_name = 'user-list')
	# scrumy_status = serializers.HyperlinkedIdentityField(many = True, read_only = True, view_name = 'status-list')
	# # scrumy_user = serializers.Field(source ='scrumy_user.username')
	# scrumy_status = serializers.HyperlinkedIdentityField(many = True, read_only = True, view_name = 'status-list')
	
	scrumy_status = serializers.PrimaryKeyRelatedField(queryset = ScrumyStatusJS.objects.all())
	scrumy_user = serializers.PrimaryKeyRelatedField(queryset = ScrumyUserJS.objects.all())
	# scrumy_status = serializers.CharField(required=True, max_length=100)
	# scrumy_user = serializers.CharField(required=True, max_length=100)
	

	def create(self, validated_data):
	# """
	# Create and return a new `Snippet` instance, given the validated data.
	# """
		return ScrumyGoalsJS.objects.create(**validated_data)

	def update(self, instance, validated_data):
		 # """
        # Update and return an existing `Snippet` instance, given the validated data.
        # ""
		instance.goals = validated_data.get('goals', instance.goals)
		instance.scrumy_status = validated_data.get('scrumy_status', instance.scrumy_status)
		instance.scrumy_user = validated_data.get('scrumy_user', instance.scrumy_user)
		instance.save()
		return instance

	class Meta:
		fields = ('id', 'goals', 'scrumy_user','scrumy_status' )
		model = ScrumyGoalsJS






class ScrumyUserJSSerializer(serializers.HyperlinkedModelSerializer):
	username = serializers.CharField(required=True, allow_blank=False, max_length=100)
	scrumygoalsjs = ScrumyGoalsSerializer(many=True, read_only=True)
	url = serializers.HyperlinkedIdentityField(view_name = 'usersjs-detail')
	
	def create(self, validated_data):
	# """
	# Create and return a new `Snippet` instance, given the validated data.
	# """
		return ScrumyUserJS.objects.create(**validated_data)

	def update(self, instance, validated_data):
		 # """
        # Update and return an existing `Snippet` instance, given the validated data.
        # ""
		instance.username = validated_data.get('username', instance.username)
		instance.save()
		return instance

	class Meta:
		fields = ('url','id', 'username', 'scrumygoalsjs')
		model = ScrumyUserJS


class ScrumyStatusJSSerializer(serializers.HyperlinkedModelSerializer):
	name = serializers.CharField(required=True, allow_blank=False, max_length=100)
	scrumygoalsjs = ScrumyGoalsSerializer(many=True, read_only=True)
	url = serializers.HyperlinkedIdentityField(view_name = 'statusjs-detail')

	def create(self, validated_data):
	# """
	# Create and return a new `Snippet` instance, given the validated data.
	# """
		return ScrumyStatusJS.objects.create(**validated_data)

	def update(self, instance, validated_data):
		 # """
        # Update and return an existing `Snippet` instance, given the validated data.
        # ""
		instance.name = validated_data.get('name', instance.name)
		instance.save()
		return instance

	
	class Meta:
		fields = ('url','id', 'name', 'scrumygoalsjs')
		model = ScrumyStatusJS