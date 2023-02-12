""" Tests for triangle.py """
import pytest
from triangle import area_of_a_triangle


def test_float_values():
    """ Test areas when values are floats """
    assert pytest.approx(area_of_a_triangle(3.4556, 8.3567)) == 14.43870626
    assert area_of_a_triangle(2.3, 5.7) == 6.555


def test_integer_values():
    """ Test areas when values are integers """
    assert area_of_a_triangle(2, 5) == 5.0
    assert area_of_a_triangle(4, 6) == 12.0


def test_zero_base():
    """ Test areas ehwn base is zero"""
    assert area_of_a_triangle(0, 5) == 0.0


def test_zero_height():
    """ Test areas when base and height are zero """
    assert area_of_a_triangle(2, 0) == 0.0


def test_zero_values():
    """ Test areas when base and height are zero"""
    assert area_of_a_triangle(0, 0) == 0.0


def test_negative_base():
    """ Test areas when base is negative """
    assert pytest.raises(ValueError, area_of_a_triangle, -2, 5)


def test_negative_height():
    """ Test that ValueError is raised when height is negative """
    assert pytest.raises(ValueError, area_of_a_triangle, 2, -5)


def test_negative_values():
    """ Test that ValueError is raised when both are negative """
    assert pytest.raises(ValueError, area_of_a_triangle, -2, -5)


def test_with_boolean():
    """ Test that TypeError is raised with boolean types """
    assert pytest.raises(TypeError, area_of_a_triangle, True, 5)
    assert pytest.raises(TypeError, area_of_a_triangle, 2, True)


def test_with_string():
    """ Test that TypeError is raised with string types """
    assert pytest.raises(TypeError, area_of_a_triangle, "base", 5)
    assert pytest.raises(TypeError, area_of_a_triangle, 2, "height")


def test_with_nulls():
    """ Test that TypeError is raised with null types """
    assert pytest.raises(TypeError, area_of_a_triangle, None, 5)
    assert pytest.raises(TypeError, area_of_a_triangle, 2, None)
