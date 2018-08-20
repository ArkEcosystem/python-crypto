import os
from configparser import ConfigParser
from datetime import datetime

from crypto.constants import TRANSACTION_FEES

config_file = os.path.abspath('config.ini')

settings = ConfigParser()
settings.read(config_file)

network = {}
fees = TRANSACTION_FEES.copy()


def set_network(network_name):
    """Set what network you want to use in the crypto library

    Args:
        network_name (str): name of a network, default ones are ARK's mainnet, devnet & testnet
    """
    global network
    network = {
        'epoch': datetime.strptime(settings.get(network_name, 'epoch'), '%Y-%m-%d %H:%M:%S'),
        'version': int(settings.get(network_name, 'version')),
        'wif': int(settings.get(network_name, 'wif')),
    }


def get_network():
    """Get settings for a selected network, default network is devnet

    Returns:
        dict: network settings (default network is devnet)
    """
    if not network:
        set_network('devnet')
    return network


def set_custom_network(epoch, version, wif):
    """Set custom network

    Args:
        epoch (datetime): chains epoch time
        version (int): chains version
        wif (int): chains wif
    """
    section_name = 'custom'
    if section_name not in settings.sections():
        settings.add_section(section_name)
    settings.set(section_name, 'epoch', epoch.strftime('%Y-%m-%d %H:%M:%S'))
    settings.set(section_name, 'version', str(version))
    settings.set(section_name, 'wif', str(wif))


def get_fee(transaction_type):
    """Get a fee for a given transaction type

    Args:
        transaction_type (int): transaction type for which we wish to get a fee

    Returns:
        int: transaction fee
    """
    return fees.get(transaction_type)


def set_fee(transaction_type, value):
    """Set a fee

    Args:
        transaction_type (int): transaction_type for which we wish to set a fee
        value (int): fee for a given transaction type
    """
    global fees
    fees[transaction_type] = value
