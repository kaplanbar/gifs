from setuptools import setup

setup(
    name='gifs',
    version='0.1.0',
    py_modules=['gifs'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'gifs = gifs:cli',
        ],
    },
)