#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import inline

@inline.c
def simd_add(a: bytes, b: bytes) -> bytes:
    """
    static char buf[16];
    char* func(const char * restrict a, const char * restrict b) {
        for (int i = 0; i < 16; i++) {
            buf[i] = 0;
        }

        for (char * restrict dest = buf; *a && *b;) {
            *dest++ = *a++ + *b++;
        }
        return buf;
    }
    """

def test_simd_add():
    assert simd_add(b'`````', b'\x08\x05\x0C\x0C\x0F') == b'hello'
