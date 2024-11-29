from crypto.transactions.types.abstract_transaction import AbstractTransaction
from crypto.utils.abi_encoder import AbiEncoder


class Vote(AbstractTransaction):
    def __init__(self, data: dict = None):
        """
        Inicializa una instancia de Vote, decodificando el payload si está presente.

        Args:
            data (dict, optional): Datos de la transacción.
        """
        payload = self.decode_payload(data or {})

        if payload is not None:
            data['vote'] = payload['args'][0]

        super().__init__(data)

    def get_payload(self) -> str:
        """
        Obtiene el payload específico para la transacción de voto.

        Returns:
            str: Payload en formato hexadecimal.
        """
        if 'vote' not in self.data:
            return ''
        encoder = AbiEncoder()
        return encoder.encode_function_call('vote', [self.data['vote']])
