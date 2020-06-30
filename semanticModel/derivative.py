import abc
from cffi import FFI
import _FDtomoC

class Derivative(object):
    def __init__(self, derivative = None):
        self.derivativeField = None
        self.elements = None
        self.column_elements = None
        self.elements_row = None
        self.jndx = None
        self.number_columns = None
        self.number_rows = None
        self.total_elements = None

    def getClass(self):
        length = 1000000
        self.elements = _FDtomoC.ffi.unpack(self.derivativeField.elements, length)
        self.column_elements = _FDtomoC.ffi.unpack(self.derivativeField.column_elements, length)
        self.elements_row = _FDtomoC.ffi.unpack(self.derivativeField.elements_row, length)
        self.jndx = _FDtomoC.ffi.unpack(self.derivativeField.jndx, length)
        self.number_columns = self.derivativeField.number_columns
        self.number_rows = self.derivativeField.number_rows
        self.total_elements = self.derivativeField.total_elements

    def getField(self):
        jndx = _FDtomoC.ffi.new("int[]", self.jndx)
        derivativeFieldPtr = _FDtomoC.ffi.new("sparse_matrix *", {'elements' : self.elements, 'column_elements' : self.column_elements, \
                                                'elements_row' : self.elements_row, 'jndx' : jndx, 'number_columns' : self.number_columns, \
                                                'number_rows' : self.number_rows, 'total_elements' : self.total_elements})