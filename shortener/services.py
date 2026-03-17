import string


BASE62 = string.digits + string.ascii_letters


def base62_encode(data: bytes) -> str:
    num = int.from_bytes(data, "big")
    if num == 0:
        return BASE62[0]

    encoded = []
    while num > 0:
        num, rem = divmod(num, 62)
        encoded.append(BASE62[rem])

    return ''.join(reversed(encoded))


def base62_decode(data: str) -> bytes:
    num = 0
    for char in data:
        num = num * 62 + BASE62.index(char)
    
    length = (num.bit_length() + 7) // 8
    return num.to_bytes(length, "big") if length > 0 else b"\x00"