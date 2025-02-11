import pytest

@pytest.fixture
def identity():
    """Identity fixture
    """
    data = {
        'data': {
            'private_key': 'bef98d4c0e58d0e4695560594f91a349421b7cdc3e63a560470ccb259f99f087',
            'public_key': '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3',
            'address': '0x6F0182a0cc707b055322CcF6d4CB6a5Aff1aEb22',
            'wif': 'SFyRYRYL1DddchRpuhp94hKN1tpYjzAEkLuUDAMjGJBkoAaz2RQk'
        },
        'passphrase': 'my super secret passphrase'
    }
    return data

@pytest.fixture
def sign_compact():
    """Identity fixture
    """
    data = {
        'data': {
            'serialized': '1f0567c4def813a66e03fa1cd499a27c6922698a67e25e0b38458d8f4bb0e581fc25fcdf9d110b82bde15bae4a49118deb83cfc3ec1656c2a29286d7836d328abe',
            'message': 'ff13b004d11523dda1efac58723ed4c63a3afe61a5464498fcb5058de20aeb7a'
        },
        'passphrase': 'my super secret passphrase'
    }
    return data

@pytest.fixture
def validator():
    """Validator fixture
    """
    return {
        'bls_public_key': 'b0093ac8f37588e15df7cfb04d0722dc5486cec062233136d3b6a16d41946577a1f332c4c29c0601ccefac1905dbb611',
        'bls_private_key': '3c0e55f46009b02bd739a16945babe797e6cbd096294dcc2550bce4baea2bde9',
        'passphrase': 'bless organ december boring ill obvious unaware dinosaur broccoli build hamster rebuild skin airport stay entry denial agent october thought duck trouble decorate way',
    }

@pytest.fixture
def bls_keys():
    """BLS private keys fixture
    """
    return [
        {
            'bls_public_key': '90507d5a1a4cde6729f61a0e8fcc34f854113faf05f995b3ffd320639c4ffd118c335099350c92daa58e9ba22ca71af1',
            'bls_private_key': '710b0de2981d407d144161a5123f498a88355e3b0a559aa7942d90d49d0d5b34',
            'passphrase': 'famous dolphin salad photo spend stock portion outdoor print fiscal element smoke silent ritual verify current better raw visual mom real bubble certain banana',
        },
        {
            'bls_public_key': 'af7f00ec30273a99411aa940ecf40646fa684f82d7d70e536a76c7c02e8ee6f3ffd297c42ad3775922938a31925bc1ab',
            'bls_private_key': '5a010d4c79c01fc4d26fcce16a601da683bd2dcb67aa09d6d4ab29042020e62b',
            'passphrase': 'good copper economy hope purity budget mistake achieve tail endless travel vibrant office cement inmate gospel effort desert garbage fiscal direct siege bright habit',
        },
        {
            'bls_public_key': '84e79b94cc89e0a95b8aaa57949f04986f00ac3c28518af5e85152cd3806159dce3a3cd371b7a9c07568c43de6c3f621',
            'bls_private_key': '311886ef722406cdad272e4930679fb06b0bbe2ba12593cc48fa93547c60ba46',
            'passphrase': 'hidden soap wall giant abuse force raw coral spy assault key parade churn reflect lounge fly yellow awkward air ocean young melody cake decide',
        },
        {
            'bls_public_key': 'aab82e8feea3ece5b7ccf99d820dc13b28f443d387ef371c8556671f2359469a5952d610624b85747ac4ba8ae9cbfb6b',
            'bls_private_key': '5432d15659b8a75a692e5800bd9c2d8f2515e45716ccb1d4b1b366447a7c1451',
            'passphrase': 'salt refuse nothing ordinary rigid exile fitness acoustic enjoy top pole miracle stem clinic range multiply worry jump question broken whip hidden annual umbrella',
        },
        {
            'bls_public_key': 'a18dfb7ba3053845bf26f9e4038cb1b964670140b855c2558d329a4a7df0ad81f413d24deb9e6edf87780b3ab2ba1f4b',
            'bls_private_key': '46180073978c64b90b062759408ed18729ee2031944cca65b0bdfa2789116949',
            'passphrase': 'bounce salon piece fire vacuum laundry welcome solution ribbon ivory street smoke birth library announce duck case refuse cry first camp what turn canal',
        },
        {
            'bls_public_key': '85caef761ec3845f5f835ea749e274ca90e3515d485219e8a3b469358f1cbf796926ef438e813db684e8f3a05b0210d8',
            'bls_private_key': '20d999f46f2d25e3338c4509faab59177310e648503e6f86818bb4a5a71b1a1f',
            'passphrase': 'always predict vocal eager pluck food check today obscure cancel coil begin muscle mistake onion fruit forget extra cousin shoulder cradle chase toss short',
        },
        {
            'bls_public_key': 'b79975e1f4eefea36eef216295b8b9d46fac639943bc5e1a8aa5815f1593b592466e0df424d5a2136e05cf3ae8e75b15',
            'bls_private_key': '2acea7bda926715a45f327a3d686bb35105b88dce85be9c80218e148402eff0a',
            'passphrase': 'slam peanut energy bright network gas subway have aerobic scare planet depth lazy claim render civil capable green panel loud venue warfare melt jelly',
        },
        {
            'bls_public_key': 'b0c002ade13cbff5f6c696e86b27ccca2ea396ccf2c7a686ab82f07ea3b38234ffd7eb6858cad6cdc09a6032e5653115',
            'bls_private_key': '03d12d4ed66ea5866cc5fd998958a3dd02d5605a34294a57ad300860c1c21b27',
            'passphrase': 'essence giant awful mixed mistake task vocal prevent room spot weird car safe mom gorilla reopen ability syrup step omit column shell rotate crumble',
        },
        {
            'bls_public_key': 'a158a42fb1862f16cdc59fa69a57d57bd86931ad856030dd28550377e69ebc586dc5cb3444c5d89a92de05cb7f5467ad',
            'bls_private_key': '664b966a562ebf45125834dd5b9505221d40bf712f679442281dd3d380b8c56a',
            'passphrase': 'this fix sort sword knee more hill into innocent idea bargain have phrase fall zebra manage casino apology leisure arch shrimp target patrol cradle',
        },
        {
            'bls_public_key': '9720ffa79fc8e9f04c153653c5cbc5bb1d2f1fc387d2640f6023585da3f3344374367240249e667d7f640fd1e0828202',
            'bls_private_key': '6237b95b32b77331fa0fc760d607f104b0bc975e789f226853d8e3f0daf985e1',
            'passphrase': 'paper ghost fatigue citizen broom radar honey success mother toilet insane all filter dutch excite kid dignity gaze exist layer elegant nerve lake silver',
        },
        {
            'bls_public_key': '870b7c4db4ca1902e3d1aaf82e993e8c78f1b66b59febf7c41aceba45abe1403136c8b32a2ab3ad66d6fa2c40a724935',
            'bls_private_key': '0bb418ef9a25dc1f4cb1568c6b29abdc262b86d6589027b002b47f65fa4fd454',
            'passphrase': 'aisle orbit train among zero correct task sell scheme combine harsh gasp scissors addict tank key trust mirror immense common barely accident industry road',
        },
        {
            'bls_public_key': '8bc136c71bd8fbb02c01ef2b90c7d0ade4f82d6275117e21e7794861487c9ce74c9e6f6470ab06a25d41b650f140a304',
            'bls_private_key': '183894353dc05c1c2bb7d3030d7638cadb951c07f560a4af79ab1a4057fccf57',
            'passphrase': 'trend exotic educate fantasy truck day amateur worth home more spice display jelly ivory swift mind assume what total often grace process dizzy payment',
        },
        {
            'bls_public_key': 'a97a89995be26a0dce2e6b53b08453eb37b6705210527cf39c40fa928fdb31b62b580794f794c52d273d650fe066bf60',
            'bls_private_key': '46c042254f22e5d779faa8c799c1b1f6673468195a367a4b328344c8fdc4572d',
            'passphrase': 'cabbage rhythm rice pelican vintage benefit soccer stove pioneer bleak fossil emerge tell pretty champion depart today lobster into abandon dignity perfect scissors silly',
        },
        {
            'bls_public_key': '8925b5568d5f97be7ba52d39c96cae06133b1deffa4b030529205ca8548e6ae0df91875aa34d59cc6fe1787f9e05f42b',
            'bls_private_key': '6191cad0ba2f8c4bc3fe148d0f4e119c117f31c3b8320bd976db5f631b761b62',
            'passphrase': 'romance eyebrow capital dinner apple video extend puppy rely pistol tissue color dynamic parade ketchup mother giraffe vintage basic risk orchard paddle another disagree',
        },
        {
            'bls_public_key': '8aefc9325c182ddc2ae8fd6825871481b28966ff6e876da7bb72db86cc8fc8df7d01e6b52b01bd5c0478f3006cdf819f',
            'bls_private_key': '1e0a8618b7e867c46ce04e1b1071977340d3a2175241878c899dceeda4fad764',
            'passphrase': 'stereo tank target husband local retreat liquid zero master shy control viable ceiling negative universe glove tomato neglect rain motion cage early cherry sock',
        },
        {
            'bls_public_key': 'b1186f7dee7d5dad1e451eb5c18ade0d9d706dd0ceea7d8407ee6e6656caadf6426f08ce8e0f31260892e685c3f4c4e1',
            'bls_private_key': '56d24d247c4cb234ce3e18a61ad94484d8c949e4df1211d28caa8115d300da2d',
            'passphrase': 'ladder where left grid stand code exercise cattle success rent air keep enhance news time six often fat similar quantum open rain bag code',
        },
        {
            'bls_public_key': '8942eb575dd8a1e0145125471eb594b7724574f92f604415d8b0c5e3056ee183e304797c033a6ad81c6c5a18de7647fd',
            'bls_private_key': '5313dc4c76303f43ad04d25274ba776268efd95dcf960ea671684a9f91fd5f7d',
            'passphrase': 'huge sorry trash price oxygen sheriff hello purchase era enrich life pole basket infant wing release injury punch inflict good much bargain pair biology',
        },
        {
            'bls_public_key': '8cacf7a6fdca95d05261ae074fb108e014022393f636a02890c27b8c3235624650f5d357cde2fc037f312a956f2a9b1b',
            'bls_private_key': '139341609069795a42a2fbbb3dcc335fdc80b86f1c473f2c7d270ed8a580467b',
            'passphrase': 'increase garbage input leaf accuse hold proud begin copy wire sell immense crop slide coach nerve food assume attack matrix text announce appear mobile',
        },
        {
            'bls_public_key': 'afe1816457e64227fb1a3da8a3141caaa4cd03937b5ba5e2b454801f4f058d1536d8e64adbb2f1a9b5e2956dcfdbe101',
            'bls_private_key': '30f661095ecd42a5e5ea0685e56accb26ebf99c635720a253139177e5acde38d',
            'passphrase': 'wine apology crew sick pet fork twelve fluid flavor perfect phrase love crime attack simple emotion smart visa keen saddle unlock foil crush neck',
        },
        {
            'bls_public_key': '84950d69eeb3d84552a61a1a4e4eaa0bf3f3c924abe9cd84f5673cdbc79bc0d664a56478b0faedce995d4367b57331cf',
            'bls_private_key': '305430a7d6571049cea36418c65c150314b6a0787af701a5a4a38237307eae5e',
            'passphrase': 'simple capital style robot duck police dose life bacon library figure wonder involve glory gallery cattle hockey balance home rigid arrive buyer crouch whale',
        },
    ]
