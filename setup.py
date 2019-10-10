from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Google Analytics Scraper',
    url='https://bitbucket.org/KyleMoore1/google-analytics-monthly-scraper/src/master/',
    author='Kyle Moore',
    # Needed to actually package something
    packages=['googleAnalyticsScraper'],
    # Needed for dependencies
    install_requires=
    [
    'httplib2',
    'oauth2client',
    'google-api-python-client',
    'google',
    'datetime',
    'gspread'
    ],

    # The license can be anything you like
    license='MIT',
    description='google analytics scraper',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
)
