from setuptools import setup

setup(
    name="mit-course-catalog-cli",
    description="Lets you access the MIT course catalog from your command line!",
    version='0.1',
    url="https://github.com/yczeng/mit-course-catalog-cli",
    download_url="https://github.com/yczeng/mit-course-catalog-cli",
    author="Catherine Zeng",
    author_email="yczeng@mit.edu",
    license="MIT",
    py_modules=['main'],
    install_requires=[
        'Click',
        'urllib',
        'pyquery',
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'],
    entry_points='''
        [console_scripts]
        mit-cc=main:cli
    ''',
)