from setuptools import setup

setup(
    name='gifs',
    version='0.1.0',
    py_modules=['gifs', 'github_actions', 'github_path_parser'],
    install_requires=[
        'Click',
        'PyGithub'
    ],
    entry_points={
        'console_scripts': [
            'gifs = gifs:cli',
        ],
    },
)