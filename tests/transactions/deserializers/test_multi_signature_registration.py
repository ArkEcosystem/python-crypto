from crypto.transactions.deserializer import Deserializer

def test_multi_signature_registration_deserializer():
    serialized = 'ff021701000000040000000000000000000205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b89600943577000000000002030205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b89603df0a1eb42d99b5de395cead145ba1ec2ea837be308c7ce3a4e8018b7efc7fdb803860d76b1df09659ac282cea3da5bd84fc45729f348a4a8e5f802186be72dc17f3b316d16f8fe2ed58abf46379126be1978f222092085d5bf3c887f6c5329956c4b1141611e57682362c0962bcadd2d68d368904aff2a4443d0e4039c984fb23c0088049c54917fd5319a33668d419efb87e9c90c274651614d89d4c5db5590b90417e7d7babb17ff49cc787e21f527757261a2d94df256606eab9f4e3b0221459b01ed57f6bdd7524cd54961d446a86552a6adcae892fcff3e1c9bae12f4c0c80f85e04a3826c992fafbbbbaa3261b72587743f3aaf21ed7dd1c3af04ffe9b3f4afb02a9518f8e314dc880d359367c77c7ec5c45c3f7c9cad129da439e2a2f3e1421adbac65f17c4615bd12fdbe9bad0856dbbdec12531d82fd0297f16b11c436c54ee'  # noqa
    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()
    data = actual.to_dict()
    assert data['asset']['multiSignature']['min'] == 2
    assert data['asset']['multiSignature']['lifetime'] == 24
    assert data['asset']['multiSignature']['publicKeys'] == [
        '0205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b896',
        '03df0a1eb42d99b5de395cead145ba1ec2ea837be308c7ce3a4e8018b7efc7fdb8',
        '03860d76b1df09659ac282cea3da5bd84fc45729f348a4a8e5f802186be72dc17f'
    ]
    # actual.verify()
