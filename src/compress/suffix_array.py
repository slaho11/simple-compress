def construct_suffix_array(data: bytes) -> list[int]:
    """Construct a suffix array - naive approach.

    O(n^2 log n) time complexity.

    """
    if not data:
        return []

    suffixes: list[tuple[int, bytes]] = []
    for i in range(len(data) + 1):
        suffixes.append((i, data[i:]))

    return [suffix[0] for suffix in sorted(suffixes, key=lambda x: x[1])]
