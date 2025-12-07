from src.compress import suffix_array
import pytest


@pytest.mark.parametrize(
    'input_data, expected',
    [
        (b'banana', [6, 5, 3, 1, 0, 4, 2]),
        (b'cabbage', [7, 1, 4, 3, 2, 0, 6, 5]),
        (b'', []),
    ],
)
def test_construct_suffix_array(input_data: bytes, expected: list[int]) -> None:
    result = suffix_array.construct_suffix_array(input_data)
    assert result == expected
