function BookmarkDetailController($scope, $routeParams, BookmarkDetailService) {
    var ctrl = this;
    var bookmark_id = $routeParams.id

    ctrl.bookmark = BookmarkDetailService.get_bookmark(bookmark_id).
    then(function success(response) {
        ctrl.bookmark = response.data;
    
    });
}

angular
  .module('bookmark')
  .controller('BookmarkDetailController', BookmarkDetailController)
