from crypto.utils.unit_converter import UnitConverter
from decimal import Decimal

def test_it_should_parse_units_into_wei():
    assert UnitConverter.parse_units(1, 'wei') == '1'
    assert UnitConverter.parse_units(1.0, 'wei') == '1'
    assert UnitConverter.parse_units('1', 'wei') == '1'
    assert UnitConverter.parse_units('1.0', 'wei') == '1'

    assert UnitConverter.parse_units(Decimal(1), 'wei') == '1'
    assert UnitConverter.parse_units(Decimal(1.0), 'wei') == '1'
    assert UnitConverter.parse_units(Decimal('1'), 'wei') == '1'
    assert UnitConverter.parse_units(Decimal('1.0'), 'wei') == '1'

def test_it_should_parse_units_into_gwei():
    assert UnitConverter.parse_units(1, 'gwei') == '1000000000'
    assert UnitConverter.parse_units(1.0, 'gwei') == '1000000000'
    assert UnitConverter.parse_units('1', 'gwei') == '1000000000'
    assert UnitConverter.parse_units('1.0', 'gwei') == '1000000000'

    assert UnitConverter.parse_units(Decimal(1), 'gwei') == '1000000000'
    assert UnitConverter.parse_units(Decimal(1.0), 'gwei') == '1000000000'
    assert UnitConverter.parse_units(Decimal('1'), 'gwei') == '1000000000'
    assert UnitConverter.parse_units(Decimal('1.0'), 'gwei') == '1000000000'

def test_it_should_parse_units_into_ark():
    assert UnitConverter.parse_units(1, 'ark') == '1000000000000000000'
    assert UnitConverter.parse_units(1.0, 'ark') == '1000000000000000000'
    assert UnitConverter.parse_units('1', 'ark') == '1000000000000000000'
    assert UnitConverter.parse_units('1.0', 'ark') == '1000000000000000000'

    assert UnitConverter.parse_units(Decimal(1), 'ark') == '1000000000000000000'
    assert UnitConverter.parse_units(Decimal(1.0), 'ark') == '1000000000000000000'
    assert UnitConverter.parse_units(Decimal('1'), 'ark') == '1000000000000000000'
    assert UnitConverter.parse_units(Decimal('1.0'), 'ark') == '1000000000000000000'

def test_it_should_parse_decimal_units_into_ark():
    assert UnitConverter.parse_units(0.1, 'ark') == '100000000000000000'
    assert UnitConverter.parse_units('0.1', 'ark') == '100000000000000000'

def test_it_should_format_units_from_wei():
    assert UnitConverter.format_units(1, 'wei') == 1.0
    assert UnitConverter.format_units(1.0, 'wei') == 1.0
    assert UnitConverter.format_units('1', 'wei') == 1.0
    assert UnitConverter.format_units('1.0', 'wei') == 1.0

    assert UnitConverter.format_units(Decimal(1), 'wei') == 1.0
    assert UnitConverter.format_units(Decimal(1.0), 'wei') == 1.0
    assert UnitConverter.format_units(Decimal('1'), 'wei') == 1.0
    assert UnitConverter.format_units(Decimal('1.0'), 'wei') == 1.0

def test_it_should_format_units_from_gwei():
    assert UnitConverter.format_units(1000000000, 'gwei') == 1.0
    assert UnitConverter.format_units('1000000000', 'gwei') == 1.0

    assert UnitConverter.format_units(Decimal(1000000000), 'gwei') == 1.0
    assert UnitConverter.format_units(Decimal('1000000000'), 'gwei') == 1.0

def test_it_should_format_units_from_ark():
    assert UnitConverter.format_units(1000000000000000000, 'ark') == 1.0
    assert UnitConverter.format_units('1000000000000000000', 'ark') == 1.0

    assert UnitConverter.format_units(Decimal(1000000000000000000), 'ark') == 1.0
    assert UnitConverter.format_units(Decimal('1000000000000000000'), 'ark') == 1.0

def test_it_should_throw_exception_for_unsupported_unit_in_parse():
    try:
        UnitConverter.parse_units(1, 'unsupported')
    except ValueError as e:
        assert str(e) == 'Unsupported unit: unsupported. Supported units are \'wei\', \'gwei\', and \'ark\'.'

def test_it_should_throw_exception_for_unsupported_unit_in_format():
    try:
        UnitConverter.format_units('1', 'unsupported')
    except ValueError as e:
        assert str(e) == 'Unsupported unit: unsupported. Supported units are \'wei\', \'gwei\', and \'ark\'.'

def test_it_should_parse_units_into_ark_with_fraction():
    assert UnitConverter.parse_units(0.1, 'ark') == '100000000000000000'
    assert UnitConverter.parse_units('0.1', 'ark') == '100000000000000000'

def test_it_should_convert_wei_to_ark():
    assert UnitConverter.wei_to_ark(1, 'DARK') == '0.000000000000000001 DARK'
    assert UnitConverter.wei_to_ark(1) == '0.000000000000000001'
    assert UnitConverter.wei_to_ark(1000000000000000000, 'DARK') == '1 DARK'
    assert UnitConverter.wei_to_ark(1000000000000000000) == '1'

    assert UnitConverter.wei_to_ark('1', 'DARK') == '0.000000000000000001 DARK'
    assert UnitConverter.wei_to_ark('1') == '0.000000000000000001'
    assert UnitConverter.wei_to_ark('1000000000000000000', 'DARK') == '1 DARK'
    assert UnitConverter.wei_to_ark('1000000000000000000') == '1'

    assert UnitConverter.wei_to_ark(Decimal(1), 'DARK') == '0.000000000000000001 DARK'
    assert UnitConverter.wei_to_ark(Decimal(1)) == '0.000000000000000001'
    assert UnitConverter.wei_to_ark(Decimal(1000000000000000000), 'DARK') == '1 DARK'
    assert UnitConverter.wei_to_ark(Decimal(1000000000000000000)) == '1'

    assert UnitConverter.wei_to_ark(Decimal('1'), 'DARK') == '0.000000000000000001 DARK'
    assert UnitConverter.wei_to_ark(Decimal('1')) == '0.000000000000000001'
    assert UnitConverter.wei_to_ark(Decimal('1000000000000000000'), 'DARK') == '1 DARK'
    assert UnitConverter.wei_to_ark(Decimal('1000000000000000000')) == '1'

def test_it_should_convert_gwei_to_ark():
    assert UnitConverter.gwei_to_ark(1, 'DARK') == '0.000000001 DARK'
    assert UnitConverter.gwei_to_ark(1) == '0.000000001'
    assert UnitConverter.gwei_to_ark(1000000000, 'DARK') == '1 DARK'
    assert UnitConverter.gwei_to_ark(1000000000) == '1'

    assert UnitConverter.gwei_to_ark('1', 'DARK') == '0.000000001 DARK'
    assert UnitConverter.gwei_to_ark('1') == '0.000000001'
    assert UnitConverter.gwei_to_ark('1000000000', 'DARK') == '1 DARK'
    assert UnitConverter.gwei_to_ark('1000000000') == '1'

    assert UnitConverter.gwei_to_ark(Decimal(1), 'DARK') == '0.000000001 DARK'
    assert UnitConverter.gwei_to_ark(Decimal(1)) == '0.000000001'
    assert UnitConverter.gwei_to_ark(Decimal(1000000000), 'DARK') == '1 DARK'
    assert UnitConverter.gwei_to_ark(Decimal(1000000000)) == '1'

    assert UnitConverter.gwei_to_ark(Decimal('1'), 'DARK') == '0.000000001 DARK'
    assert UnitConverter.gwei_to_ark(Decimal('1')) == '0.000000001'
    assert UnitConverter.gwei_to_ark(Decimal('1000000000'), 'DARK') == '1 DARK'
    assert UnitConverter.gwei_to_ark(Decimal('1000000000')) == '1'
