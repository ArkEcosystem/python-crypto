from crypto.networks.abstract_network import AbstractNetwork

class Testnet(AbstractNetwork):
    def chain_id(self):
        return 11812

    def epoch(self):
        return '2017-03-21T13:00:00.000Z'

    def wif(self):
        return 'ba'
