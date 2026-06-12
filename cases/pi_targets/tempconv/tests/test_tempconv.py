from converter import c_to_f, f_to_c


def test_freezing_point():
    assert c_to_f(0) == 32


def test_boiling_point():
    assert c_to_f(100) == 212


def test_room_temperature():
    assert c_to_f(20) == 70


def test_inverse_conversion():
    assert f_to_c(212) == 100
