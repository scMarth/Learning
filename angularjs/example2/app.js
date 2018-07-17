var myApp = angular.module('myApp', []);

// controller takes a name and a function
myApp.controller('mainController', function($scope){
   $scope.name = 'Jane Doe';
   $scope.occupation = 'Coder';
   $scope.getName = function() {
      return 'John Doe';
   }

   console.log($scope);
});

var searchPeople = function(firstName, lastName, height, age, occupation){
   return 'Jane Doe';
}

// console.log(searchPeple(1,2,3,4,5));
// console.log(searchPeple); // this returns a string


// parses the stringified function and returns an array containing the parameters of the function
console.log(angular.injector().annotate(searchPeople));



