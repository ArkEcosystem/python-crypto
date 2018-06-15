import setuptools

requires = [

]

tests_require = [
    'flake8>=3.5.0',
    'flake8-import-order>=0.17.1',
    'flake8-quotes>=1.0.0',
]

extras_require = {
    'test': tests_require,
    'dev': requires + tests_require
}

setuptools.setup(
    name='ark-crypto',
    description='A simple Cryptography Implementation in Python for the ARK Blockchain.',
    version='0.0.1',
    author='',
    author_email='',
    url='https://github.com/ArkEcosystem/python-crypto',
    packages=[
        'ark',
    ],
    install_requires=requires,
    extras_require=extras_require,
    tests_require=tests_require,
)
