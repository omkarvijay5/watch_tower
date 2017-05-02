function BookmarkCreateController($scope, $routeParams, $http, $location) {

    // create a blank bookmark object to handle form data.
    $scope.bookmark = {};
    
    // calling our bookmark create function.
    $scope.createBookmark = function() {
        // Posting data to create bookmakr
        $http({
            method  : 'POST',
            url     : '/api/bookmarks/',
            data    : $scope.bookmark,
            headers : {'Content-Type': 'application/json'},
        })
        
        .then(function(success) {
            // Success redirect to the bookmarks list page
            $location.path( "#!" );

        }, function(error){
            
            // Showing errors.
            if (error.data.name) {
                $scope.errorName = error.data.name[0];
            } else {
                $scope.errorName = ''
            }
            if(error.data.url){
                $scope.errorUrl = error.data.url[0];
            }  else {
              $scope.errorUrl = ''
            }

        });
    };

}

angular
  .module('bookmark')
  .controller('BookmarkCreateController', BookmarkCreateController)
