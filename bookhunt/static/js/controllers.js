function BooksCtrl($scope, bookhunt, $resource) {
    $resource('/api/v1/book/').get(function(response){
        $scope.books = response.objects;
    });
    $scope.orderProp = 'code';
    
}
