from py_solving_suite.encoder import encode
from py_solving_suite.decoder import decode

def test_encode_decode():
    original = "Hello World!"
    encoded = encode(original)
    decoded = decode(encoded)
    assert decoded == original
