import pytest

from src.compress import bwt


@pytest.mark.parametrize(
    'input_data, expected',
    [
        (b'bananabar', (b'nnbbraaaa', 4)),
        (b'Humble Bundle', (b'e emnllbduuHB', 2)),
        (b'Mellow Yellow', (b'ww MYeelllloo', 1)),
        (b'', (b'', 0)),
    ],
)
def test_encode(input_data: bytes, expected: tuple[bytes, int]) -> None:
    result = bwt.encode(input_data)
    assert result == expected


@pytest.mark.parametrize(
    'input_data, marker, expected',
    [
        (b'nnbbraaaa', 4, b'bananabar'),
        (b'e emnllbduuHB', 2, b'Humble Bundle'),
        (b'ww MYeelllloo', 1, b'Mellow Yellow'),
        (b'', 0, b''),
    ],
)
def test_decode(input_data: bytes, marker: int, expected: bytes) -> None:
    result = bwt.decode(input_data, marker)
    assert result == expected


@pytest.mark.parametrize(
    'input_data',
    [
        b'The quick brown fox jumps over the lazy dog.',
        b'1234567890!@#$%^&*()_+-=[]{}|;:\'",.<>/?`~',
        b'a' * 1000,
    ],
)
def test_encode_decode_roundtrip(input_data: bytes) -> None:
    encoded, marker = bwt.encode(input_data)
    decoded = bwt.decode(encoded, marker)
    assert decoded == input_data
