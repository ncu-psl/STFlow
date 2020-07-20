from cffi import FFI
import _FDtomoC

class Point(object):
    def __init__(self, x = None, y = None, z = None):
        self.x = x
        self.y = y
        self.z = z
        self.pointField = None

    def getField(self):
        pointFieldPtr = _FDtomoC.ffi.new("Point3D *", {'x' : self.x, 'y' : self.y, 'z':self.z})
        return pointFieldPtr[0]

    def getClass(self):
        self.x = self.pointField.x
        self.y = self.pointField.y
        self.z = self.pointField.z

class PointDouble(object):
    def __init__(self, x = None, y = None, z = None):
        self.x = x
        self.y = y
        self.z = z
        self.pointField = None

    def getField(self):
        pointFieldPtr = _FDtomoC.ffi.new("Point3DDouble *", {'x' : self.x, 'y' : self.y, 'z':self.z})
        return pointFieldPtr[0]

    def getClass(self):
        self.x = self.pointField.x
        self.y = self.pointField.y
        self.z = self.pointField.z

    def createOrigin(self, file = None):
        origin = PointDouble()
        tmp = _FDtomoC.ffi.new("char[]", file.encode('ascii'))
        origin.pointField = _FDtomoC.lib.createOrigin(tmp)
        origin.getClass()
        return origin