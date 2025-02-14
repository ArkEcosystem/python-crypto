from crypto.utils.unit_converter import UnitConverter

def test_it_should_parse_units_into_wei():
    wei_value = UnitConverter.parse_units(1, 'wei')

    assert wei_value == '1'

def test_it_should_parse_units_into_gwei():
    gwei_value = UnitConverter.parse_units(1, 'gwei')

    assert gwei_value == '1000000000'

def test_it_should_parse_units_into_ark():
    ark_value = UnitConverter.parse_units(1, 'ark')

    assert ark_value == '1000000000000000000'

def test_it_should_parse_decimal_units_into_ark():
    ark_value_decimal = UnitConverter.parse_units(0.1, 'ark')

    assert ark_value_decimal == '100000000000000000'

def test_it_should_format_units_from_wei():
    formatted_value = UnitConverter.format_units('1', 'wei')

    assert formatted_value == 1.0

def test_it_should_format_units_from_gwei():
    formatted_value = UnitConverter.format_units('1000000000', 'gwei')

    assert formatted_value == 1.0

def test_it_should_format_units_from_ark():
    formatted_value = UnitConverter.format_units('1000000000000000000', 'ark')

    assert formatted_value == 1.0

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
    ark_value = UnitConverter.parse_units(0.1, 'ark')

    assert ark_value == '100000000000000000'

def test_it_should_convert_wei_to_ark():
    assert UnitConverter.wei_to_ark(1, 'DARK') == '0.000000000000000001 DARK'
    assert UnitConverter.wei_to_ark(1) == '0.000000000000000001'
    assert UnitConverter.wei_to_ark('1000000000000000000', 'DARK') == '1 DARK'
    assert UnitConverter.wei_to_ark('1000000000000000000') == '1'

def test_it_should_convert_gwei_to_ark():
    assert UnitConverter.gwei_to_ark(1, 'DARK') == '0.000000001 DARK'
    assert UnitConverter.gwei_to_ark(1) == '0.000000001'
    assert UnitConverter.gwei_to_ark('1000000000', 'DARK') == '1 DARK'
    assert UnitConverter.gwei_to_ark('1000000000') == '1'
