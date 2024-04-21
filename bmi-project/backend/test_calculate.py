from backend.calculate import calculate_bmi, get_bmi_category
import pytest


def test_calculate_bmi():
    assert calculate_bmi(160.0, 54.0) == 21.09


def test_calculate_bmi_zero_and_negative_values():
    assert calculate_bmi(0.0, 0.0) == 0
    assert calculate_bmi(-1.0, 0.0) == 0
    assert calculate_bmi(0.0, -1.0) == 0
    assert calculate_bmi(150.0, 0.0) == 0
    assert calculate_bmi(0.0, 150.0) == 0


def test_invalid_input_type():
    with pytest.raises(TypeError):
        calculate_bmi('160', 54)

    with pytest.raises(TypeError):
        calculate_bmi(160, '54')

    with pytest.raises(TypeError):
        calculate_bmi('160', '54')

    with pytest.raises(TypeError):
        calculate_bmi('a', 55)

    with pytest.raises(TypeError):
        calculate_bmi(55, 'a')

    with pytest.raises(TypeError):
        calculate_bmi('a', 'a')


def test_category():
    assert get_bmi_category(0.0) == 'غیر طبیعی'
    assert get_bmi_category(16.0) == 'کمبود وزن'
    assert get_bmi_category(21.1) == 'وزن نرمال'
    assert get_bmi_category(28.0) == 'اضافه وزن'
    assert get_bmi_category(31.0) == 'چاقی'


def test_invalid_category_input():
    with pytest.raises(TypeError):
        get_bmi_category('16.0')

