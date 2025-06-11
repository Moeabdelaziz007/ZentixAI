import math
import pytest

from plugin_example import CalculatorPlugin


@pytest.fixture
def plugin():
    return CalculatorPlugin()


def test_addition_integers(plugin):
    assert plugin.execute({"a": 2, "b": 3})["result"] == 5


def test_addition_floats(plugin):
    result = plugin.execute({"a": 2.5, "b": 3.5})["result"]
    assert math.isclose(result, 6.0)


def test_addition_int_float_combinations(plugin):
    assert plugin.execute({"a": 2, "b": 3.5})["result"] == 5.5
    assert plugin.execute({"a": 2.5, "b": 3})["result"] == 5.5


def test_extremely_large_integers(plugin):
    big = 10 ** 100
    assert plugin.execute({"a": big, "b": big})["result"] == big * 2


def test_extremely_small_floats(plugin):
    result = plugin.execute({"a": 1e-308, "b": 1e-308})["result"]
    assert math.isclose(result, 2e-308)


def test_float_overflow_raises(plugin):
    with pytest.raises(OverflowError):
        plugin.execute({"a": 1e308, "b": 1e308})


def test_invalid_type_raises(plugin):
    with pytest.raises(TypeError):
        plugin.execute({"a": "1", "b": 1})


def test_missing_argument_raises(plugin):
    with pytest.raises(ValueError):
        plugin.execute({"a": 1})


def test_infinite_input(plugin):
    with pytest.raises(OverflowError):
        plugin.execute({"a": float("inf"), "b": 1})


def test_nan_input(plugin):
    with pytest.raises(ValueError):
        plugin.execute({"a": float("nan"), "b": 1})
