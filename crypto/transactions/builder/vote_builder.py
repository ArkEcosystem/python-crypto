from crypto.transactions.builder.base import AbstractTransactionBuilder
from crypto.transactions.types.vote import Vote


class VoteBuilder(AbstractTransactionBuilder):
    def vote(self, vote: str):
        """
        Establece el campo 'vote' en los datos de la transacción.

        Args:
            vote (str): Dirección a la que se vota.

        Returns:
            self: Instancia del builder para encadenar métodos.
        """
        self.transaction.data['vote'] = vote
        self.transaction.refresh_payload_data()
        return self

    def get_transaction_instance(self, data: dict):
        """
        Crea una instancia de la transacción Vote con los datos proporcionados.

        Args:
            data (dict): Datos de la transacción.

        Returns:
            Vote: Instancia de la transacción Vote.
        """
        return Vote(data)
