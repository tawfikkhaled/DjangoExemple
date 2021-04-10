define(["require", "exports"], function (require, exports) {
    "use strict";
    exports.__esModule = true;
    exports.run = exports.DEBUG = void 0;
    exports.DEBUG = false;
    function run(widgetFullName, options) {
        console.log("executing run");
    }
    exports.run = run;
});
