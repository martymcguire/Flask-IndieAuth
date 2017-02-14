"""
Flask-IndieAuth
-------------

Allows requests to be authenticated with https://indieauth.com/
"""
from setuptools import setup

setup(
    name='Flask-IndieAuth',
    version='0.0.3.1',
    url='https://github.com/martymcguire/flask-indieauth/',
    license='MIT',
    author='Marty McGuire',
    author_email='mail@martymcgui.re',
    description='Allow requests to be authenticated with https://indieauth.com/',
    long_description=__doc__,
    py_modules=['flask_indieauth'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
