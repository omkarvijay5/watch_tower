function BookmarkListController($scope, $resource, BookmarkListService) {
    var ctrl = this;

    ctrl.bookmarks = BookmarkListService.get_bookmarks().
    then(function success(response) {
        var bookmarks = response.data;
        ctrl.bookmarks = bookmarks
    
    });
}

angular
  .module('bookmark')
  .controller('BookmarkListController', BookmarkListController)
