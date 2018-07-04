	$http({
			url: '127.0.0.1:8000/usersjs/?format=json',
			method: 'post',
			data: {username: $scope.username},
			headers: {'content-Type': 'application/json'}
		}).then(function onSuccess(response) {
			console.log(response);
		}).catch(function onError(error){
			console.log(error);
		});




app.factory('Entry', function($resource) {
		return $resource('usersjs');
	}

		);




.when('/', 
		{
			controller: 'myCtrl',
			templateUrl: '/static/pages/add_user_btn.html'
		})
	.when('/NewTask', 
		{
			controller: 'myCtrl',
			templateUrl: '/static/pages/add_task_btn.html'
		})
	.when('/AddTask', 
		{
			controller: 'myCtrl',
			templateUrl: '/static/pages/add_task.html'
		})
	.when('/AddUser', 
		{
			controller: 'myCtrl',
			templateUrl: '/static/pages/add_user.html'
		});
	$locationProvider.hashPrefix('');








		 $scope.master = {}; 
    $scope.update = function(newUser) {
       $scope.master = angular.copy(newUser); 
     };
      $scope.reset = function() {
        $scope.newUser = angular.copy($scope.master); 
     }; 
    $scope.reset();


    from rest_framework import serializers
from .models import ScrumyUser, ScrumyGoals, ScrumyStatus, ScrumyStatusJS, ScrumyUserJS, ScrumyGoalsJS



class ScrumyStatusSerializer(serializers.HyperlinkedModelSerializer):

	
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



















class ScrumyStatusJSSerializer(serializers.HyperlinkedModelSerializer):
	scrumygoalsjs = ScrumyGoalsSerializer(many=True, read_only=True)
	
	class Meta:
		fields = ('id', 'name')
		model = ScrumyStatusJS



class ScrumyGoalsJSSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)
	goals = serializers.CharField(style={'base_template': 'textarea.html'})
	scrumy_user_id = serializers.CharField(required=True, allow_blank=False, max_length=100)
	scrumy_status_id = serializers.CharField(required=True, allow_blank=False, max_length=100)

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
		instance.scrumy_user_id = validated_data.get('scrumy_user_id', instance.scrumy_user_id)
		instance.scrumy_status_id = validated_data.get('scrumy_status_id', instance.scrumy_status_id)
		instance.save()
		return instance

	class Meta:
		fields = ('id', 'goals', 'scrumy_user_id', 'scrumy_status_id')
		model = ScrumyGoalsJS






class ScrumyUserJSSerializer(serializers.HyperlinkedModelSerializer):
	username = serializers.CharField(required=True, allow_blank=False, max_length=100)
	scrumygoalsjs = ScrumyGoalsSerializer(many=True, read_only=True)
	
	def create(self, validated_data):
	# """
	# Create and return a new `Snippet` instance, given the validated data.
	# """
		return ScrumyUserJS.objects.create(**validated_data)

	def update(self, instance, validated_data):
		 # """
        # Update and return an existing `Snippet` instance, given the validated data.
        # ""
		instance.username = validated_data.get('goals', instance.username)
		instance.save()
		return instance

	class Meta:
		fields = ('id', 'username', 'scrumygoalsjs')
		model = ScrumyUserJS





































// ////////////////////////////////////Mr. Mat/////////////////////////////

app.controller('myCtrl', function($scope, $http) {

	getGoals();
	getUsers();
	getGoalsJS();
	getUsersJS();


	function getUsers(){
		$http.get("http://127.0.0.1:8000/users/?format=json").then(function(response) {
			$scope.users = angular.fromJson(response.data);
		});
	};

	function getGoals(){
		$http.get("http://127.0.0.1:8000/goals/?format=json").then(function(response) {
			$scope.goals = angular.fromJson(response.data);
		});	
	};

	// ///////////////////////////////////////////////////////////

	function getUsersJS(){
		$http.get("http://127.0.0.1:8000/usersjs/?format=json").then(function(response) {
			$scope.usersJS = angular.fromJson(response.data);
		});
	};

	function getGoalsJS(){
		$http.get("http://127.0.0.1:8000/goalsjs/?format=json").then(function(response) {
			$scope.goalsJS = angular.fromJson(response.data);
		});	
	};


	$scope.addGoal = function(){

		console.log('submit button clicked');

		$http.post('http://127.0.0.1:8000/goalsjs/?format=api', {'goals': $scope.goal, 'scrumy_user_id': user_id, 'scrumy_status_id': 1 })
		.success(function(data){
			if (data==true){
				getGoals();
			}
		});	
	};


	$scope.addUser = function (){
		$http.post('http://127.0.0.1:8000/usersjs/?format=api', {'username': $scope.username})
		.success(function(data){
			if (data==true){
				getUsers();
			}
		});		
	};


	


	
    $scope.firstName= "Johneeee";
    $scope.lastName= "Doeeee";
    $scope.email= "fasugbab@gmail.com";
    $scope.phone_no= "09098737336";
    $scope.headerValue  = "my static scrumy";
    $scope.changeHeader = function(){
    	$scope.headerValue = "My dynamic Scrumy";
    	}


    $scope.taskName = null;
	$scope.addTask = function(){
    	var data = { Name: $scope.taskName };
    	$http.post("http://127.0.0.1:8000/users/?format=json", data)
    	.success(function(data,status,headers)	{
    		alert('Task Added Successfully');
    	$http.get(headers('location')).success(function(data){
    		$scope.goals.push(data);
    	});
    	});
    	};


});


// app.config(function($routeProvider, $locationProvider)	{
// 	$routeProvider
// 	.when('adduser', 
// 		{
// 			controller: 'myCtrl',
// 			templateUrl: '/static/pages/page1.html'
// 		})
// 	.when('addtask', 
// 		{
// 			controller: 'myCtrl',
// 			templateUrl: 'page1.html'
// 		})
// 	.otherwise({
// 		redirect: '/'
// 		});
// 	$locationProvider.hashPrefix('');
// });

app.config(function($routeProvider, $locationProvider)	{
	$routeProvider
	.when('/', 
		{
			controller: 'myCtrl',
			templateUrl: '/static/pages/add_user_btn.html'
		})
	.when('/NewTask', 
		{
			controller: 'myCtrl',
			templateUrl: '/static/pages/add_task_btn.html'
		})
	.when('/AddTask/:id[0-9]', 
		{
			controller: 'myCtrl',
			templateUrl: '/static/pages/add_task.html'
		})
	.when('/AddUser', 
		{
			controller: 'myCtrl',
			templateUrl: '/static/pages/add_user.html'
		});
	$locationProvider.hashPrefix('');
	
});


app.directive("myDirective", function() {
    return {
    	 restrict : "A",
        template : "<h1>this is an angularJS Directive created by me</h1>"
    };
});


































////////////////////////////////////////////////////serializer.py//////////////
from rest_framework import serializers
from .models import ScrumyUser, ScrumyGoals, ScrumyStatus, ScrumyStatusJS, ScrumyUserJS, ScrumyGoalsJS



class ScrumyStatusSerializer(serializers.HyperlinkedModelSerializer):

	
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



















class ScrumyStatusJSSerializer(serializers.HyperlinkedModelSerializer):
	scrumygoalsjs = ScrumyGoalsSerializer(many=True, read_only=True)

	

	def update(self, instance, validated_data):
		 # """
        # Update and return an existing `Snippet` instance, given the validated data.
        # ""
		instance.username = validated_data.get('goals', instance.username)
		instance.save()
		return instance
	
	class Meta:
		fields = ('id', 'name')
		model = ScrumyStatusJS



class ScrumyGoalsJSSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)
	goals = serializers.CharField(style={'base_template': 'textarea.html'})
	scrumy_user_id = serializers.CharField(required=True, allow_blank=False, max_length=100)
	scrumy_status_id = serializers.CharField(required=True, allow_blank=False, max_length=100)

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
		instance.scrumy_user_id = validated_data.get('scrumy_user_id', instance.scrumy_user_id)
		instance.scrumy_status_id = validated_data.get('scrumy_status_id', instance.scrumy_status_id)
		instance.save()
		return instance

	class Meta:
		fields = ('id', 'goals', 'scrumy_user_id', 'scrumy_status_id')
		model = ScrumyGoalsJS






class ScrumyUserJSSerializer(serializers.HyperlinkedModelSerializer):
	username = serializers.CharField(required=True, allow_blank=False, max_length=100)
	scrumygoalsjs = ScrumyGoalsSerializer(many=True, read_only=True)
	
	def create(self, validated_data):
	# """
	# Create and return a new `Snippet` instance, given the validated data.
	# """
		return ScrumyUserJS.objects.create(**validated_data)

	def update(self, instance, validated_data):
		 # """
        # Update and return an existing `Snippet` instance, given the validated data.
        # ""
		instance.username = validated_data.get('goals', instance.username)
		instance.save()
		return instance

	class Meta:
		fields = ('id', 'username', 'scrumygoalsjs')
		model = ScrumyUserJS
