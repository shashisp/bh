angular.module('bookhunt', ['ngResource'], function ($interpolateProvider){
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
}).factory('bookhunt', ['$http', function($http){

    var bookhunt = function(data) {
        angular.extend(this, data);
    };


    bookhunt.getAll = function() {
        return $http.get('/api/v1/book/').then(function(response) {
            return response.data.objects;
        });
    };

   

    return bookhunt;
}]);