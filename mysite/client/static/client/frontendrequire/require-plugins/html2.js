define('html2', [], function () {

    function regexpEscape(text) {
        return text.replace(/[-[\]{}()*+?.,\\^$|#\s]/g, "\\$&");
    }

    function defragmentUrl(url) {
        var index = url.indexOf("#");
        var region = null, path = url;
        if (index > -1)
            return [url.substr(0, index), url.substr(index + 1)];
        return [url, null];
    }

    function getRegion(value, region) {
        if (region == null || region.length == 0)
            return value;
        var startPattern = "<!--\\s*#region\\s+" + regexpEscape(region) + "\\s*-->";
        var regexStart = new RegExp(startPattern, "ig");
        var match = regexStart.exec(value);
        if (match != null && match.length != 0) {
            var regexStop = /<!--\s*#((end)?region).*-->/gi;
            var substring = match.input.substring(match.index + match[0].length);
            var stopMatch;
            var depth = 1;
            while ((stopMatch = regexStop.exec(substring)) != null) {
                if (/^region/i.test(stopMatch[1]))
                    depth = depth + 1;
                else
                    depth = depth - 1;
                if (depth == 0) {
                    var s = stopMatch.input.substr(0, stopMatch.index);
                    return s;
                }
                if (depth < 0) {
                    console.warn("Region overlapping");
                    return value;
                }
            }
            console.warn("Cannot find end region " + region);
            return value;
        }
        else {
            console.warn("Cannot find region " + region);
            return value;
        }
    }

    return {

        load: function (name, req, onload, config) {
            var defragmented = defragmentUrl(name);
            var path = defragmented[0];
            var region = defragmented[1];
            req(["text!" + path], function (value) {
                if (region != null && region.length > 0)
                    value = getRegion(value, region);
                onload({ "default": value });
            });
        }
    };
});