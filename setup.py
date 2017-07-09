from setuptools import setup

setup(
    name="mit-course-catalog-cli",
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        cc=main:cli
    ''',
)