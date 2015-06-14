
var bookhunt = angular.module("bookhunt", ["bookServices", ]).config(function(
            $interpolateProvider, $httpProvider) {

    // Fix the conflict between django template variables
    // and angular template variables.
    $interpolateProvider.startSymbol("[[");
    $interpolateProvider.endSymbol("]]");



});
