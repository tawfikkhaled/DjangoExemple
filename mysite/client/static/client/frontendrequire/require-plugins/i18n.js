// requirejs plugin to load i18n resources as AMD dependencies with the prefix "i18n!"
define('i18n', ['i18next'], function (i18next) {
    return {
        load: function (name, req, onload, config) {
            i18next.loadNamespaces([name], function () { return onload(""); });
        }
    };
});