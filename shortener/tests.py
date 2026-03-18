from .services import base62_encode


def test_same_input_same_output():
    phrase = "Hello, world!"
    incrementalsim = 1

    combined = (str(incrementalsim) + phrase).encode("utf-8")

    result = (base62_encode(combined))

    assert result == base62_encode(combined)
