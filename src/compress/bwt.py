"""Burrows-Wheeler Transform (BWT)."""


def encode(data: bytes) -> tuple[bytes, int]:
    """Encode data using BWT.

    Args:
        data: Input data to encode.

    Returns:
        A tuple containing:
            - The BWT transformed data as bytes.
            - The index where the original data would be located in the sorted rotations.

    """
    if not data:
        return b'', 0

    table = sorted([data[i:] + data[:i] for i in range(len(data))])
    last_column = bytes([row[-1] for row in table])
    marker = table.index(data)
    return last_column, marker


def decode(data: bytes, marker: int) -> bytes:
    """Decode data encoded with BWT.

    Args:
        data: BWT encoded data.
        marker: Index where the original data would be located in the sorted rotations.

    Returns:
        The original decoded data.

    """

    def tag_with_occurrence(data: bytes) -> list[tuple[int, int]]:
        counter = {}
        result = []
        for byte in data:
            counter[byte] = counter.get(byte, 0) + 1
            result.append((byte, counter[byte]))

        return result

    tagged_data = tag_with_occurrence(data)
    tagged_data_positions = {tag: i for i, tag in enumerate(tagged_data)}
    sorted_tagged_data = tag_with_occurrence(sorted(data))

    i = marker
    result = []
    for _ in range(len(data)):
        byte = sorted_tagged_data[i]
        result.append(byte[0])
        i = tagged_data_positions[byte]

    return bytes(result)
