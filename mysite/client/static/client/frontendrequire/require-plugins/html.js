// requirejs plugin to load html resources as AMD dependencies with the prefix "html!"
define('html', [], function () {
    return {
        load: function (name, req, onload, config) {
            req(["text!../" + name], function (value) {
                onload(value);
            });
        }
    };
});