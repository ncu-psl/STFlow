import abc
from cffi import FFI
import _FDtomoC

class ResidualVector(object):
    def __init__(self, residual_vector = None):
        self.residualField = None
        self.residual_vector = residual_vector

    def getClass(self):
        self.residual_vector = _FDtomoC.ffi.unpack(self.residualField, 50000000)

    def getField(self):
        residualFieldPtr = _FDtomoC.ffi.new("float[]", self.residual_vector)
        return residualFieldPtr[0]