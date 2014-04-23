var sys    = require('sys'),
    fs     = require('fs'),
    sass   = require('node-sass'),
    source = '';

process.stdin.resume();
process.stdin.setEncoding('utf8');

process.stdin.on('data', function(chunk) {
    source += chunk;
});

process.stdin.on('end', function() {
    sass.render({
        data: source,
        // outputStyle: 'nested|compressed',
        // sourceComments: 'none|normal',
        // includePaths: [],
        success: function (css, err) {
            if (err) {
                throw err;
            }            
            process.stdout.write(css);
        }
    })
});