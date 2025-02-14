# import numpy as np
from decimal import Decimal
from typing import Union

class UnitConverter:
    WEI_MULTIPLIER = '1'
    GWEI_MULTIPLIER = '1000000000'  # 1e9
    ARK_MULTIPLIER = '1000000000000000000'  # 1e18

    @staticmethod
    def parse_units(value: Union[float, int, str, Decimal], unit='ark') -> str:
        value = Decimal(str(value))

        unit = unit.lower()
        if unit == 'wei':
            return format((value * Decimal(UnitConverter.WEI_MULTIPLIER)).normalize(), 'f')

        if unit == 'gwei':
            return format((value * Decimal(UnitConverter.GWEI_MULTIPLIER)).normalize(), 'f')

        if unit == 'ark':
            return format((value * Decimal(UnitConverter.ARK_MULTIPLIER)).normalize(), 'f')

        raise ValueError(f"Unsupported unit: {unit}. Supported units are 'wei', 'gwei', and 'ark'.")

    @staticmethod
    def format_units(value: Union[float, int, str, Decimal], unit='ark') -> Decimal:
        value = Decimal(str(value))

        unit = unit.lower()
        if unit == 'wei':
            return value / Decimal(UnitConverter.WEI_MULTIPLIER)

        if unit == 'gwei':
            return value / Decimal(UnitConverter.GWEI_MULTIPLIER)

        if unit == 'ark':
            return value / Decimal(UnitConverter.ARK_MULTIPLIER)

        raise ValueError(f"Unsupported unit: {unit}. Supported units are 'wei', 'gwei', and 'ark'.")

    @staticmethod
    def wei_to_ark(value: Union[float, int, str, Decimal], suffix=None):
        converted_value = UnitConverter.format_units(UnitConverter.parse_units(value, 'wei'), 'ark')
        converted_value = format(converted_value.normalize(), 'f')

        if suffix is not None:
            return f"{converted_value} {suffix}"

        return str(converted_value)

    @staticmethod
    def gwei_to_ark(value: Union[float, int, str, Decimal], suffix=None):
        converted_value = UnitConverter.format_units(UnitConverter.parse_units(value, 'gwei'), 'ark')
        converted_value = format(converted_value.normalize(), 'f')

        if suffix is not None:
            return f"{converted_value} {suffix}"

        return str(converted_value)
