from control_tools.interpolation import interpolate, interpolate_with_limits

def test_simple():
    result = interpolate(5,0,10,0,1)
    assert result == 0.5

def test_simple_low_limit():
    result = interpolate(0,0,10,0,1)
    assert result == 0

def test_simple_high_limit():
    result = interpolate(10,0,10,0,1)
    assert result == 1

def test_simple_high_limit_e():
    result = interpolate(15,0,10,0,1)
    assert result == 1.5

def test_simple_high_with_limit():
    result = interpolate_with_limits(15,0,10,0,1)
    assert result == 1.0