#-*- coding: utf-8 -*-

import os
import unittest

from gears.environment import Environment
from gears.finders import FileSystemFinder

from gears_sass import SASSCompiler


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
SCSS_DIR = os.path.join(ROOT_DIR, 'fixtures', 'scss')
CSS_DIR = os.path.join(ROOT_DIR, 'fixtures', 'css')
OUTPUT_DIR = os.path.join(ROOT_DIR, 'fixtures', 'output')


def fixture_load(name):
    f = open(os.path.join(SCSS_DIR, "%s.scss" % name), 'r')
    src_scss = f.read()
    f.close()

    f = open(os.path.join(CSS_DIR, "%s.css" % name), 'r')
    src_css = f.read()
    f.close()

    f = open(os.path.join(OUTPUT_DIR, "%s.css" % name), 'r')
    src_output = f.read()
    f.close()

    return src_scss, src_css, src_output


class CompilerTest(unittest.TestCase):

    def setUp(self):
        self.compiler = SASSCompiler()

        self.env = Environment(root=OUTPUT_DIR, public_assets=(r'.*\.css',),
                               fingerprinting=False)
        self.env.finders.register(FileSystemFinder([SCSS_DIR]))
        self.env.compilers.register('.scss', self.compiler.as_handler())
        self.env.register_defaults()
        self.env.save()

    def test_syntax(self):
        scss, css, output = fixture_load('syntax')
        self.assertEqual(css, output)

    def test_variables(self):
        scss, css, output = fixture_load('variables')
        self.assertEqual(css, output)

    def test_mixin(self):
        scss, css, output = fixture_load('mixin')
        self.assertEqual(css, output)

    def test_import(self):
        scss, css, output = fixture_load('import')
        self.assertEqual(css, output)
