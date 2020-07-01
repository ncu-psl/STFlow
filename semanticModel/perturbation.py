import abc
from cffi import FFI
import _FDtomoC
import sys
class Perturbation(object):
    def __init__(self):
        self.perturbationField = None
        self.n = None
        self.x = None
        self.jndx = None
        self.se = None
        self.tmp = None

    def getClass(self):
        self.n = self.perturbationField.n
        self.x = _FDtomoC.ffi.unpack(self.perturbationField.x, 2500000)
        self.jndx = _FDtomoC.ffi.unpack(self.perturbationField.jndx, 3000000)
        self.se = _FDtomoC.ffi.unpack(self.perturbationField.se, 2500000)
        
    def getField(self):
        self.tmp = { 'x' : _FDtomoC.ffi.new("float[]", self.x), \
                   'jndx' : _FDtomoC.ffi.new("int[]", self.jndx), \
                   'se'  : _FDtomoC.ffi.new("float[]", self.se)}
        perturbationFieldPtr = _FDtomoC.ffi.new("RUNLSQR_DATA *")
        perturbationFieldPtr.x = self.tmp['x']
        perturbationFieldPtr.jndx = self.tmp['jndx']
        perturbationFieldPtr.se = self.tmp['se']
        perturbationFieldPtr.n = self.n
        return perturbationFieldPtr[0]
        