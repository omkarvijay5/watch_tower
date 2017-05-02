function BookmarkEditController($scope, $routeParams, $http, $location, BookmarkDetailService) {

    // create a blank bookmark object to handle form data.
    $scope.bookmark = {};

    var bookmark_id = $routeParams.id
    
    // calling our submit function to update the bookmark
    $scope.editBookmark = function() {
        // updating data to update bookmakr
        $http({
            method  : 'PUT',
            url     : '/api/bookmarks/' + bookmark_id.toString() + '/',
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

    $scope.bookmark = BookmarkDetailService.get_bookmark(bookmark_id).
    then(function success(response) {
        $scope.bookmark = response.data;
    
    });

}

angular
  .module('bookmark')
  .controller('BookmarkEditController', BookmarkEditController)
