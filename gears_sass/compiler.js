var sys    = require('util'),
    fs     = require('fs'),
    sass   = require('node-sass'),
    source = '';

process.stdin.resume();
process.stdin.setEncoding('utf8');

process.stdin.on('data', function(chunk) {
    source += chunk;
});

process.stdin.on('end', function() {
    sass.render(source, function(err, css) {
        if (err) {
            throw err;
        }
        process.stdout.write(css);
    });
});