//
requirejs.config({
    // baseUrl: 'js/lib',
    paths: {
        // the left side is the module ID,
        // the right side is the path to
        // the jQuery file, relative to baseUrl.
        // Also, the path should NOT include
        // the '.js' file extension. This example
        // is using jQuery 1.9.0 located at
        // js/lib/jquery-1.9.0.js, relative to
        // the HTML page.
        jquery: 'jquery-1.11.3'
    }
});

// main.js
require(['wtf', 'jquery'], function (math, $){
    var x = math.add(1,1);
    $('h1').text('jquery works!')

    console.log(x);
    console.log($);
});
