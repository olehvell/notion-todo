from setuptools import setup, find_packages

setup(
    name='todo',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'todo=todo.cli:main',
        ],
    },
)