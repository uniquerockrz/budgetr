from setuptools import setup

setup (
    name='ledgerlib',
    version='0.0.1',
    packages=['ledgerlib', 'ledgerlib.ledger'],
    install_requires=[
        'pandas==2.0.3'
    ]
)