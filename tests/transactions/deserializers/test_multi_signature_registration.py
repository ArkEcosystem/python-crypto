from crypto.transactions.deserializer import Deserializer


def test_multi_signature_registration_deserializer():
    serialized = 'ff011e0100000004000500000000000000023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d30065cd1d00000000000203029fab3cb2f5e248ae7cbb4de646741da4d73c493b2a03ab5c71507fb2c0dcca9203629f9dbf7f1e91cefa845126189816ceae357bdd1f41bd14787318a7d5b55d48027941d2059f89a26d89e87d3385e261a0ede1234aaeaa487012b69d6b67962dc504aee2652b4a41350b9821c261bb0a3c3492146a6e0ebda4e28a185d6c2e9eb7702b4889e8b9b5fadd989e71dbb7527b3be071e15cf3a93165e8f1b8c7b16974008c7c7018082d9afddd70652f559377a941240cf797819fe02f657d4509c8bcb133156741163cfb8e9b4db6ef398bdd5f94a24e1f0134d04783391bc13370201b015306973b045d83191ce57c56f097b79c0771a94310ee67aed8b96e1bb7f497e451fe569c297a857f840f46b801534179e87a5e07015fb03727746be450e925d6021d03e19f1e39ac9b985b867e8362002df387fd778a682218bc3e6ce4b5c7f59eaa6f893ffb8deec2e4c9b28287417e2ab7b427356ca74d790f7fb63b6f8dcbd5'  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()
    data = actual.to_dict()

    assert data['amount'] == 0
    assert data['nonce'] == 5
    assert data['version'] == 1
    assert data['network'] == 30
    assert data['typeGroup'] == 1
    assert data['fee'] == 500000000
    assert data['senderPublicKey'] == '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3'
    assert data['signature'] == '04aee2652b4a41350b9821c261bb0a3c3492146a6e0ebda4e28a185d6c2e9eb7702b4889e8b9b5fadd989e71dbb7527b3be071e15cf3a93165e8f1b8c7b16974'
    assert data['id'] == '75affed80fcad541787fd673fafa6b90561feac2d3f4a2dae857641109c44787'
    assert data['asset']['multiSignature']['min'] == 2
    assert data['asset']['multiSignature']['publicKeys'] == [
        '029fab3cb2f5e248ae7cbb4de646741da4d73c493b2a03ab5c71507fb2c0dcca92',
        '03629f9dbf7f1e91cefa845126189816ceae357bdd1f41bd14787318a7d5b55d48',
        '027941d2059f89a26d89e87d3385e261a0ede1234aaeaa487012b69d6b67962dc5'
    ]
    assert data['signatures'] == [
        '008c7c7018082d9afddd70652f559377a941240cf797819fe02f657d4509c8bcb133156741163cfb8e9b4db6ef398bdd5f94a24e1f0134d04783391bc13370201b',  # noqa
        '015306973b045d83191ce57c56f097b79c0771a94310ee67aed8b96e1bb7f497e451fe569c297a857f840f46b801534179e87a5e07015fb03727746be450e925d6',  # noqa
        '021d03e19f1e39ac9b985b867e8362002df387fd778a682218bc3e6ce4b5c7f59eaa6f893ffb8deec2e4c9b28287417e2ab7b427356ca74d790f7fb63b6f8dcbd5'  # noqa
    ]

    actual.verify_schnorr_multisig()
