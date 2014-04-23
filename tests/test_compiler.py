#-*- coding: utf-8 -*-

import os
import unittest

from gears.environment import Environment
from gears.finders import FileSystemFinder

from gears_sass import SASSCompiler


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
ASSETS_DIR = os.path.join(ROOT_DIR, 'fixtures', 'assets')
STATIC_DIR = os.path.join(ROOT_DIR, 'fixtures', 'output')


def fixture_path(name):
    return os.path.join(ASSETS_DIR, name)


def fixture_load(name):
    asset_scss, asset_css = "%s.scss" % name, "%s.css" % name

    f_scss = open(fixture_path(asset_scss), 'r')
    src_scss = f_scss.read()
    f_scss.close()

    f_css = open(fixture_path(asset_css), 'r')
    src_css = f_css.read()
    f_css.close()

    return src_scss, src_css


class CompilerTest(unittest.TestCase):

    def setUp(self):
        self.compiler = SASSCompiler()

        self.env = Environment(STATIC_DIR)
        self.env.finders.register(FileSystemFinder([ASSETS_DIR]))
        self.env.compilers.register('.scss', self.compiler)
        self.env.register_defaults()

    def test_syntax(self):
        scss, css = fixture_load('syntax')
        print self.compiler.run(scss)
        # self.env.save()
        # self.assertEqual(css, css)
