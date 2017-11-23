# -*- coding: utf-8 -*-
"""
    Autop Tests
    ~~~~~~~~~~~~
    Tests the Autop application.
"""

from setuptools import setup, find_packages


setup(
    name='autop',
    version='1.0',
    description='Autop Test Application',
    author='Ashay Chitnis',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
     'beautifulsoup4==4.6.0',
     'certifi==2017.11.5',
     'chardet==3.0.4',
     'click==6.7',
     'docutils==0.14',
     'Flask==0.12.2',
     'Flask-Bootstrap==3.3.7.1',
     'idna==2.6',
     'itsdangerous==0.24',
     'Jinja2==2.10',
     'jmespath==0.9.3',
     'MarkupSafe==1.0',
     'python-dateutil==2.6.1',
     'requests==2.18.4',
     's3transfer==0.1.11',
     'six==1.11.0',
     'urllib3==1.22',
     'Werkzeug==0.12.2'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
