gears-sass
==================

SASS/SCSS compiler for Gears. 

Installation
------------

Install `gears-sass` with pip:

    $ pip install gears-sass


Requirements
------------

- [node.js](http://nodejs.org)
- [node-sass](https://github.com/andrew/node-sass)


Usage
-----

Add `gears_sass.SASSCompiler` to `environment`'s compilers registry:

    from gears_sass import SASSCompiler
    environment.compilers.register('.scss', SASSCompiler.as_handler())

If you use Gears in your Django project, add this code to its settings:

    GEARS_COMPILERS = {
        '.scss': 'gears_sass.SASSCompiler',
    }


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/ChillyBwoy/gears-sass/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

