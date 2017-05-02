function BookmarkDeleteController($scope, $routeParams, $http, $location) {
    
    // calling our submit function.
    $scope.deleteBookmark = function(bookmark_id) {
        // Posting data to create bookmakr
        $http({
            method  : 'DELETE',
            url     : '/api/bookmarks/' + bookmark_id.toString() + '/',
            data    : {},
            headers : {'Content-Type': 'application/json'},
        })
        
        .then(function(success) {
            // Success redirect to the bookmarks list page
            $location.path( "#!" );

        });
    };

}

angular
  .module('bookmark')
  .controller('BookmarkDeleteController', BookmarkDeleteController)
