"""RLE, Run-Length Encoding, in binary format.

Each piece of information has a fixed, known size:
    first byte: count byte
    second byte: data_byte

"""


def encode(data: bytes) -> bytes:
    if not data:
        return b''

    current_byte = data[0]
    count = 1
    result = []
    for byte in data[1:]:
        if byte == current_byte and count < 255:
            count += 1
        else:
            result.append(bytes([count, current_byte]))
            current_byte = byte
            count = 1

    # Handling of the last character.
    result.append(bytes([count, current_byte]))

    return b''.join(result)


def decode(data: bytes) -> bytes:
    if not data:
        return b''

    result = []
    for i in range(0, len(data), 2):
        count = data[i]
        value = data[i + 1]
        result.append(bytes([value]) * count)

    return b''.join(result)
