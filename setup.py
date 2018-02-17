from setuptools import setup

setup(
    name='bellybutton',
    packages=['bellybutton'],
    platforms='any',
    version='0.0.1',
    description='Custom Python linting through AST expressions.',
    author='H. Chase Stevens',
    author_email='chase@chasestevens.com',
    url='https://github.com/hchasestevens/bellybutton',
    license='MIT',
    install_requires=[
        'astpath[xpath]>=0.6.1',
        'pyyaml>=3.12',
    ],
    tests_require=['pytest>=3.1.2', 'future>=0.16.0'],
    extras_require={'dev': ['pytest>=3.1.2', 'future>=0.16.0']},
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ]
)