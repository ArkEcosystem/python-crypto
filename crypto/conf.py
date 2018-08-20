import os
from configparser import ConfigParser
from datetime import datetime

from crypto.exceptions import ArkNetworkSettingsException

config_file = os.path.abspath('config.ini')

settings = ConfigParser()
settings.read(config_file)

network = {}


def use_network(network_name):
    """Select what network you want to use in the crypto library

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
    """Get settings for a selected network

    Returns:
        dict: network settings
    """
    if not network:
        raise ArkNetworkSettingsException('Network has not been set')
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
