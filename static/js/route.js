var bookmark = angular.module('bookmark', ["ngRoute", "ngResource"]);


var TEMPLATE_CONFIG = '/static/templates/'

bookmark.config(function($routeProvider) {
    $routeProvider
    .when("/", {
        templateUrl: TEMPLATE_CONFIG + "bookmark/bookmarks.html",
        controller: 'BookmarkListController',
        controllerAs: '$ctrl'
    }).
    otherwise({redirectTo: '/'})
});
