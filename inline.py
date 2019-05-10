#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import inspect
import ctypes
import tempfile
import distutils.ccompiler
from pathlib import Path


def c(func):
    source_code = func.__doc__
    sig = inspect.signature(func)
    module = compile_link_and_load(source_code)
    func = module.func
    func.restype = ctypes.c_char_p
    return func


################################## Compiler ##################################

def compile_link_and_load(source_code):
    name = str(hash(source_code))
    with tempfile.TemporaryDirectory() as tempdir_name:
        tempdir = Path(tempdir_name)
        source_file = tempdir / r'{name}.c'
        source_file.write_text(source_code, encoding='UTF-8')

        cc = distutils.ccompiler.new_compiler()
        object_files = cc.compile([str(source_file)], tempdir_name, extra_preargs=['-fPIC'])
        cc.link_shared_lib(object_files, tempdir / name)

        return ctypes.CDLL(tempdir / f'lib{name}.so')
