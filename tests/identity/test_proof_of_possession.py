import pytest

from crypto.configuration.network import Network
from crypto.exceptions import InvalidProofOfPossessionException
from crypto.identity.proof_of_possession import POP_DST, ProofOfPossession
from crypto.networks.testnet import Testnet

# Resolvable only once proof_of_possession has added the bundled BLS lib to sys.path
from ec import G1FromBytes, G2FromBytes  # noqa: E402, I100
from schemes import core_verify_mpl  # noqa: E402, I100, I201

SECRET_KEY = '67d53f170b908cabb9eb326c3c337762d59289a8fec79f7bc9254b584b73265c'
REGISTRANT = '0x75545540230d5c3BEf023202d23CB74cFA723376'
OTHER_REGISTRANT = '0x1E6747BEAa5B4076a6A98D735DF8c35a70D18Bdd'


class ReferenceNetwork(Testnet):
    def chain_id(self):
        return 10_000


@pytest.fixture
def reference_network():
    previous = Network.get_network()
    Network.set_network(ReferenceNetwork())
    yield
    Network.set_network(previous)


def verify(pop: dict, chain_id: int, registrant_address: str) -> bool:
    public_key = bytes.fromhex(pop['pk'])
    signature = G2FromBytes(bytes.fromhex(pop['pop']))
    message = ProofOfPossession.build_message(chain_id, registrant_address, public_key)

    return core_verify_mpl(G1FromBytes(public_key), message, signature, POP_DST)


def test_it_matches_the_reference_vector(reference_network):
    pop = ProofOfPossession.build_proof_of_possession(bytes.fromhex(SECRET_KEY), REGISTRANT)

    assert pop['pk'] == (
        'a7e75af9dd4d868a41ad2f5a5b021d653e31084261724fb4'
        '0ae2f1b1c31c778d3b9464502d599cf6720723ec5c68b59d'
    )
    assert pop['pop'] == (
        'a892e94d8ed6d0fe8792dcb31b7c5116a7d138ad4bbbd044'
        '780a7c314e86673e783850121dc34d0edfa2a2560c2f30a4'
        '02f4fa5106ff71d5c69bc3027210ef90b3d3ae0a19ffc9f5'
        '54b37aca72f3bb25788c3177514d94e041441ba9d029b3ba'
    )


def test_it_builds_a_100_byte_message():
    message = ProofOfPossession.build_message(10_000, REGISTRANT, bytes(48))

    assert len(message) == 100
    assert message[:32] == (10_000).to_bytes(32, 'big')
    assert message[32:52] == bytes.fromhex(REGISTRANT[2:])


def test_it_binds_to_the_configured_chain_id_and_registrant():
    pop = ProofOfPossession.build_proof_of_possession(bytes.fromhex(SECRET_KEY), REGISTRANT)
    chain_id = Network.get_network().chain_id()

    assert verify(pop, chain_id, REGISTRANT) is True
    assert verify(pop, chain_id + 1, REGISTRANT) is False
    assert verify(pop, chain_id, OTHER_REGISTRANT) is False


def test_it_accepts_a_lowercase_registrant():
    checksummed = ProofOfPossession.build_proof_of_possession(bytes.fromhex(SECRET_KEY), REGISTRANT)
    lowercase = ProofOfPossession.build_proof_of_possession(
        bytes.fromhex(SECRET_KEY), REGISTRANT.lower()
    )

    assert lowercase == checksummed


@pytest.mark.parametrize('registrant_address', [
    '',
    None,
    '75545540230d5c3BEf023202d23CB74cFA723376',
    '0x75545540230d5c3BEf023202d23CB74cFA72337',
    '0x75545540230d5c3BEf023202d23CB74cFA7233766',
    '0x75545540230d5c3BEf023202d23CB74cFA72337g',
    '0x75545540230d5c3bEf023202d23CB74cFA723376',
])
def test_it_rejects_an_invalid_registrant(registrant_address):
    with pytest.raises(InvalidProofOfPossessionException):
        ProofOfPossession.build_proof_of_possession(bytes.fromhex(SECRET_KEY), registrant_address)


def test_it_rejects_an_invalid_registrant_from_passphrase(passphrase):
    with pytest.raises(InvalidProofOfPossessionException):
        ProofOfPossession.from_passphrase(passphrase, '0xinvalid')
