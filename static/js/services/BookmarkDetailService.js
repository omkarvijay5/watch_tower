var bookmark = angular.module('bookmark')

bookmark.factory('BookmarkDetailService', function($http) {
  var data = {};
  data.get_bookmark = function (bookmark_id) {
    return $http({
        method : "GET",
        url : "/api/bookmarks/" + bookmark_id.toString()
    })
  }
  return data
});
