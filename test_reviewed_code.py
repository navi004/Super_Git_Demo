from reviewed_code import sum_even_numbers
import pytest

def test_sum_even_numbers_valid_input():
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12

def test_sum_even_numbers_empty_list():
    with pytest.raises(ValueError):
        sum_even_numbers([])

def test_sum_even_numbers_none_input():
    with pytest.raises(TypeError):
        sum_even_numbers(None)

def test_sum_even_numbers_non_integer_input():
    with pytest.raises(TypeError):
        sum_even_numbers([1, 2, '3', 4, 5, 6])

def test_sum_even_numbers_negative_numbers():
    assert sum_even_numbers([-1, -2, -3, -4, -5, -6]) == -2 - 4 - 6

def test_sum_even_numbers_zero():
    assert sum_even_numbers([0, 0, 0]) == 0

def test_sum_even_numbers_large_numbers():
    assert sum_even_numbers([1000, 2000, 3000]) == 6000

def test_sum_even_numbers_single_element():
    assert sum_even_numbers([2]) == 2

def test_sum_even_numbers_no_even_numbers():
    assert sum_even_numbers([1, 3, 5]) == 0

def test_sum_even_numbers_float_input():
    with pytest.raises(TypeError):
        sum_even_numbers([1.0, 2.0, 3.0])

def test_sum_even_numbers_mixed_input():
    with pytest.raises(TypeError):
        sum_even_numbers([1, 2, '3', 4.0, 5])

def test_sum_even_numbers_empty_string_input():
    with pytest.raises(TypeError):
        sum_even_numbers([''])

def test_sum_even_numbers_list_with_none():
    with pytest.raises(TypeError):
        sum_even_numbers([1, 2, None, 4, 5])