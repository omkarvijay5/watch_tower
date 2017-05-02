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

    .when("/bookmarks/create", {
        templateUrl: TEMPLATE_CONFIG + "bookmark/bookmark_create.html",
        controller: 'BookmarkCreateController',
        controllerAs: '$ctrl'
    }).
    otherwise({redirectTo: '/'})

    .when("/bookmarks/:id", {
        templateUrl: TEMPLATE_CONFIG + "bookmark/bookmark_detail.html",
        controller: 'BookmarkDetailController',
        controllerAs: '$ctrl'
    }).
    otherwise({redirectTo: '/'})


});
