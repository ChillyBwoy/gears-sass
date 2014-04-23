gears-sass
==================

SCSS compiler for Gears. 

Bundled [node-sass](https://github.com/andrew/node-sass) version: 0.8.6


Installation
------------

Install `gears-sass` with pip:

    $ pip install gears-sass


Requirements
------------
- [node.js](http://nodejs.org)


Usage
-----

Add `gears_sass.SASSCompiler` to `environment`'s compilers registry:

    from gears_sass import SASSCompiler
    environment.compilers.register('.scss', SASSCompiler.as_handler())

If you use Gears in your Django project, add this code to its settings:

    GEARS_COMPILERS = {
        '.scss': 'gears_sass.SASSCompiler',
    }
