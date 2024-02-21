from setuptools import setup, find_packages

setup(
    name='MyPackages',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='http://github.com/<WilsonZitha>/<package-name>',
    author='<WilsonZitha>',
    author_email='<zitha66@gmail.com>'
)