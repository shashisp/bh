angular.module("bookServices", [])

.config(function($httpProvider) {
    $httpProvider.defaults.headers.post["Content-Type"] = "application/json;";
})


.factory("bookService", function($resource) {
    var url = "/api/v1/book/:id",
        book = $resource(url, {
            id: "@id"
        }, {
            submit: {
                url: url + "/submit/",
                method: "POST",
            }
        });

    return book;
})



;