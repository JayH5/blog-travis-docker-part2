import os

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):  # Stolen from txacme
    with open(os.path.join(HERE, *parts)) as f:
        return f.read()


setup(
    name='blog-travis-docker',
    version='0.1.3',
    license='BSD-3-Clause',
    url='https://github.com/JayH5/blog-travis-docker-part2',
    description='Code for a blog post on using Docker with Travis CI',
    long_description=read('README.rst'),
    author='Jamie Hewland',
    author_email='jamie@praekelt.org',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hello = blog_travis_docker.__main__:main',
        ]
    }
)
