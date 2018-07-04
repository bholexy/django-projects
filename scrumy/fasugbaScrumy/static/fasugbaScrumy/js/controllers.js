
app.controller('myCtrl', function($scope, $http, $routeParams, $location) {


	getGoals();
	getUsers();
	getGoalsJS();
	getUsersJS();
	getStatusJS();


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
			$scope.usersJS = response.data;
		});
	};

	function getGoalsJS(){
		$http.get("http://127.0.0.1:8000/goalsjs/?format=json").then(function(response) {
			$scope.goalsJS = response.data;
		});	
	};

	function getStatusJS(){
		$http.get("http://127.0.0.1:8000/statusjs/?format=json").then(function(response) {
			$scope.statusJS = response.data;
		});	
	};

$scope.addGoal1 = function(){
	$http({
	              url : "http://127.0.0.1:8000/goalsjs/",
	              method: "POST",
	              data : {
	                task : $scope.goal,
	                target_name : $scope.status,
	                user_name : $scope.user
	            },
	              headers : {'Content-Type' : 'application/json'}
	          }).then(function onSuccess(response) {
	              console.log(response);
	          }).catch(function onError(error) {
	              console.log(error);
	          });
	    };


	$scope.addGoal = function(){
		$scope.task_user_id = $routeParams.id
		console.log($routeParams.id)
		console.log($scope.task_user_id)
		console.log($scope.user);
		$http.post('http://127.0.0.1:8000/goalsjs/?format=json', 
			{
				'goals': $scope.goal,
				'scrumy_status': $scope.status, 
				'scrumy_user': $routeParams.id				 
			})
		// .success(function(data){
		// 	if (data==true){
		// 		getGoals();
		// 	}
		// });
		.then(function onSuccess(response) {
              console.log(response);
          }).catch(function onError(error) {
              console.log(error);
          });	
	};

/*
	$scope.addGoal = function (){
		console.log($scope.user);
		$http.post('http://127.0.0.1:8000/goalsjs/?format=api', {'username': $scope.username})
		.success(function(data){
			if (data==true){
				getUsers();
			}
		});		
	};
*/

	$scope.addUser = function (){
		console.log('submit button clicked');
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
	.when('/AddTask/id/:id?', 
		// .when('/AddTask/id/:id[0-9]*', 
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


// $routeProvider.when('/taskurl/', {template : "<form ng-controller='formCtrl'>"  +

//     "<p>task:<input type='text' ng-model='myTask' value=''></p>" +

//             "<p>user: <select ng-model='myName'><option ng-repeat='user in user' ng-value='user.url'>{{user.username}}</option></select></p> " +

//             "<p>status: <select ng-model='myStatus'><option ng-repeat='statu in status' ng-value='statu.url'>{{statu.target}}</option></select></p>" +

//             "<input type='submit' value='add task' ng-click='postData()'>" +

//         "</form>" })



app.directive("myDirective", function() {
    return {
    	 restrict : "A",
        template : "<h1>this is an angularJS Directive created by me</h1>"
    };
});


































