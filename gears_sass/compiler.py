import os

from gears.compilers import ExecCompiler


class SASSCompiler(ExecCompiler):
    result_mimetype = 'text/css'
    executable = 'node'
    params = [os.path.join(os.path.dirname(__file__), 'compiler.js')]

    def __init__(self, *args, **kwargs):
        self.paths = []
        super(SASSCompiler, self).__init__(*args, **kwargs)

    def __call__(self, asset):
        self.asset = asset
        super(SASSCompiler, self).__call__(asset)

    def run(self, src):
        return super(SASSCompiler, self).run(src)

    def get_args(self):
        args = super(SASSCompiler, self).get_args()
        args.append(os.path.dirname(self.asset.absolute_path))
        args.extend(self.paths)
        return args
