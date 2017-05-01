var bookmark = angular.module('bookmark')

bookmark.factory('BookmarkListService', function($http) {
  var data = {};
  data.get_bookmarks = function () {
    return $http({
        method : "GET",
        url : "/api/bookmarks/"
    })
  }
  return data
});

