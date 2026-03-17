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
