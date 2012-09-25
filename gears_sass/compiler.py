import os
from gears.compilers import ExecCompiler

class SASSCompiler(ExecCompiler):
    result_mimetype = 'text/css'
    executable = 'node'
    params = [os.path.join(os.path.dirname(__file__), 'compiler.js')]