import pytest

from src.compress import rle


DATA = bytes(
    [
        2,
        ord('a'),  # 2 a's
        3,
        ord('c'),  # 3 c's
        1,
        ord('b'),  # 1 b
        3,
        ord('d'),  # 3 d's
    ]
)


def test_encode() -> None:
    result = rle.encode('aacccbddd'.encode())
    expected = DATA
    assert result == expected


def test_decode() -> None:
    result = rle.decode(DATA)
    expected = 'aacccbddd'.encode()
    assert result == expected


@pytest.mark.parametrize(
    'input_data',
    ['', 'aaa', 'aab', 'abb', f'{"a" * 254}b', f'{"a" * 255}b', f'{"a" * 256}b'],
)
def test_encode_decode(input_data: str) -> None:
    """Test that encoding followed by decoding returns the original data."""
    encoded_input_data = input_data.encode()
    result = rle.decode(rle.encode(encoded_input_data))
    assert result == encoded_input_data
