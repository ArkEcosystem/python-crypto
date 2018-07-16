# ARK Python - Crypto

<p align="center">
    <img src="https://github.com/ArkEcosystem/python-crypto/blob/master/banner.png" />
</p>

> A simple Cryptography Implementation in Python for the ARK Blockchain.

[![Build Status](https://img.shields.io/travis/ArkEcosystem/python-crypto/master.svg?style=flat-square)](https://travis-ci.org/ArkEcosystem/python-crypto)
[![Latest Version](https://img.shields.io/github/release/ArkEcosystem/python-crypto.svg?style=flat-square)](https://github.com/ArkEcosystem/python-crypto/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Contributions are closed

We will not be accepting new PRs until we are happy with the base of the client and until it has good test coverage. We'll let you know on our #python Slack channel once we'll accept PRs again.

### AIP11 Serialization
- [ ] Transfer
- [ ] Second Signature Registration
- [ ] Delegate Registration
- [ ] Vote
- [ ] Multi Signature Registration
- [ ] IPFS
- [ ] Timelock Transfer
- [ ] Multi Payment
- [ ] Delegate Resignation

### AIP11 Deserialization
- [ ] Transfer
- [ ] Second Signature Registration
- [ ] Delegate Registration
- [ ] Vote
- [ ] Multi Signature Registration
- [ ] IPFS
- [ ] Timelock Transfer
- [ ] Multi Payment
- [ ] Delegate Resignation

### Transaction Signing
- [ ] Transfer
- [ ] Second Signature Registration
- [ ] Delegate Registration
- [ ] Vote
- [ ] Multi Signature Registration

### Transaction Verifying
- [ ] Transfer
- [ ] Second Signature Registration
- [ ] Delegate Registration
- [ ] Vote
- [ ] Multi Signature Registration

### Transaction Entity
- [ ] getId
- [ ] sign
- [ ] secondSign
- [ ] parseSignatures
- [ ] serialize
- [ ] deserialize
- [ ] toBytes
- [ ] toArray
- [ ] toJson

### Message
- [ ] sign
- [ ] verify
- [ ] toArray
- [ ] toJson

### Address Identity
- [ ] fromPassphrase
- [ ] fromPublicKey
- [ ] fromPrivateKey
- [ ] validate

### Private Key Identity
- [ ] fromPassphrase
- [ ] fromHex

### Public Key Identity
- [ ] fromPassphrase
- [ ] fromHex

### WIF Identity
- [ ] fromPassphrase

### Configuration
- [ ] getNetwork
- [ ] setNetwork
- [ ] getFee
- [ ] setFee

### Slot
- [ ] time
- [ ] epoch

### Networks (Mainnet, Devnet & Testnet)
- [ ] epoch
- [ ] version
- [ ] nethash
- [ ] wif

## Installation

```bash
...
```

## Guide for contributing

Before you start contributing please take some time and check our official [Python Development Guidelines](https://github.com/ArkEcosystem/development-guidelines/blob/master/Python/README.md) which follow the widely accepted PEP8 Python Style Guide. 🖋

1. Fork the repository on GitHub.
2. Run the tests to confirm they all pass on your system. If they don’t, you’ll need to investigate why they fail. If you’re unable to diagnose this yourself raise it as a bug report.
3. Make your change.
4. Write tests that demonstrate your bug or feature.
5. Run the entire test suite again, confirming that all tests pass including the ones you just added.
6. Send a GitHub Pull Request. GitHub Pull Requests are the expected method of code collaboration on this project.

If you have any questions, requests or ideas open an issue or ask us in #python on [ARK's Slack](https://ark.io/slack).

## Security

If you discover a security vulnerability within this package, please send an e-mail to security@ark.io. All security vulnerabilities will be promptly addressed.

## Credits

- [Rok Halužan](https://github.com/roks0n)
- [Tomaž Šifrer](https://github.com/tsifrer)
- [Brian Faust](https://github.com/faustbrian)
- [All Contributors](../../../../contributors)

## License

[MIT](LICENSE) © [ArkEcosystem](https://ark.io)
