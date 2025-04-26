import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("mouse", "Mouse"),
        ("cat", "Cat"),
        ("dog", "Dog"),
    ]
)
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("123abc", "123abc"),
        ("", ""),
        ("   ", "   "),
    ]
)
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   mouse", "mouse"),
    ]
)
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),
    ]
)
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("mouse", "s", True),
        ("cat", "f", False),
    ]
)
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("", "", True),
        ("123", "4", False),
    ]
)
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("mouse", "s", "moue"),
        ("cat is red", "ca", "t is red"),
    ]
)
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    []
)
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
