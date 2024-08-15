import sys

import setuptools


requires = [
    'base58',
    'binary-helpers',
    'blspy @ git+https://github.com/ArkEcosystem/bls-signatures@aa453d3ee99667a0f0bf25018d279e21f2b5f0b9#egg=blspy',
    'coincurve',
    'pycryptodomex',
    'btclib',
    'cryptography',
]

tests_require = [
    'flake8>=3.5.0',
    'flake8-import-order>=0.17.1',
    'flake8-print>=3.1.0',
    'flake8-quotes>=1.0.0',
    'pytest>=3.6.1',
    'pytest-cov>=2.5.1',
]

extras_require = {
    'test': tests_require,
    'dev': requires + tests_require
}

setup_requires = ['pytest-runner'] if {'pytest', 'test', 'ptr'}.intersection(sys.argv) else []

setuptools.setup(
    name='arkecosystem-crypto',
    description='A simple Cryptography Implementation in Python for the Ark Blockchain.',
    version='2.0.0',
    author='Ark Ecosystem',
    author_email='info@ark.io',
    url='https://github.com/ArkEcosystem/python-crypto',
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    install_requires=requires,
    extras_require=extras_require,
    tests_require=tests_require,
    setup_requires=setup_requires,
)
