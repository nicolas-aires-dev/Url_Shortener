from .services import base62_encode


def test_same_input_same_output():
    link = "Hello, world!"
    incrementalsim = 1

    combined = (str(incrementalsim) + link).encode("utf-8")

    result = (base62_encode(combined))

    assert result == base62_encode(combined)
