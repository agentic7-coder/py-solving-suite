"""Decoder module - Caesar cipher decoding"""

from .encoder import encode

def decode(text, shift=3):
    """Decode text that was encoded with Caesar cipher"""
    return encode(text, -shift)
