from setuptools import setup

setup(
    name="mit-course-catalog-cli",
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'Click',
        'urllib',
        'pyquery',
    ],
    entry_points='''
        [console_scripts]
        mit-cc=main:cli
    ''',
)