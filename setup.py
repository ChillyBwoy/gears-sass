import os
from setuptools import setup, find_packages

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name='gears-sass',
    version='0.1',
    license='ISC',
    author='Eugene Cheltsov',
    author_email='chill.icp@gmail.com',
    description='SASS compiler for Gears',
    long_description=read('README.md'),
    packages=find_packages(),
    include_package_data=True,
    keywords = 'gears django-gears gears-sass gears-scss',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)