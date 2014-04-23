var sys    = require('sys'),
    fs     = require('fs'),
    sass   = require('node-sass'),
    paths  = process.argv.slice(2),
    source = '';

process.stdin.resume();
process.stdin.setEncoding('utf8');

process.stdin.on('data', function(chunk) {
    source += chunk;
});

process.stdin.on('end', function() {
    sass.render({
        data: source,
        outputStyle: 'nested',      //nested|compressed|expanded
        sourceComments: 'none',     //none|normal
        includePaths: paths || [],
        success: function (css, err) {
            if (err) {
                throw err;
            }
            process.stdout.write(css);
        }
    })
});