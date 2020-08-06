import abc
from cffi import FFI
from coordinate import Coordinate1D, Coordinate3D
import _FDtomoC

class VelocityModel(object):
    def __init__(self):
        self.coordinate = Coordinate1D()
        self.velocity = None
        self.modelField = None
        self.modelFieldPtr = None

    @abc.abstractmethod
    def create(self):
        return NotImplemented

    @abc.abstractmethod
    def transform(self):
        return NotImplemented


class VelocityModel1D(VelocityModel):
    def loadVpVs(self, file):
        vpModel = VelocityModel1D()
        vsModel = VelocityModel1D()
        interp = _FDtomoC.ffi.new("char *")
        vpModelField = _FDtomoC.ffi.new("velocityModel1D *")
        vsModelField = _FDtomoC.ffi.new("velocityModel1D *")
        tmp = _FDtomoC.ffi.new("char[]", file.encode('ascii'))
        _FDtomoC.lib.readVelocityModel1D(tmp, vpModelField, vsModelField, interp)
        vpModel.modelField = vpModelField[0]
        vpModel.coordinate.coordinateField = vpModelField[0].coordinate
        vpModel.coordinate.mesh.meshField = vpModelField[0].coordinate.mesh
        vsModel.modelField = vsModelField[0]
        vsModel.coordinate.coordinateField = vsModelField[0].coordinate
        vsModel.coordinate.mesh.meshField = vsModelField[0].coordinate.mesh
        vpModel.getClass()
        vsModel.getClass()
        return vpModel, vsModel

    def transform(self, coordinate1D):
        model = VelocityModel1D()
        tmp = ""
        for i in range(coordinate1D.coordinateField.mesh.numberOfNode):
            tmp = tmp + 'I'
        tmp = _FDtomoC.ffi.new("char[]", tmp.encode('ascii'))
        model.modelField = _FDtomoC.lib.transform1D(coordinate1D.coordinateField, self.modelField, tmp)
        return model        
        
    def getField(self):
        coodinateField = self.coordinate.getField()
        velocity = _FDtomoC.ffi.new("float[]", self.velocity)
        modelField = _FDtomoC.lib.createModel3D(coodinateField, velocity)

    def getClass(self):
        self.coordinate.getClass()
        size = self.coordinate.mesh.numberOfNode
        self.velocity = _FDtomoC.ffi.unpack(self.modelField.velocity, int(size))    


class VelocityModel3D(VelocityModel):
    def __init__(self):
        self.coordinate = Coordinate3D()
        self.velocity = None
        self.modelField = None
        self.modelFieldPtr = None

    def generateFrom1D(self, coordinate3D, model1D):
        model3D = VelocityModel3D()
        model3D.modelField = _FDtomoC.lib.create3DModel(coordinate3D.coordinateField, model1D.modelField)
        model3D.coordinate.coordinateField = model3D.modelField.coordinate
        model3D.coordinate.mesh.meshField = model3D.modelField.coordinate.mesh
        model3D.coordinate.mesh.numberOfNode.pointField = model3D.modelField.coordinate.mesh.numberOfNode
        model3D.coordinate.origin.pointField = model3D.modelField.coordinate.origin
        model3D.coordinate.space.pointField = model3D.modelField.coordinate.space
        model3D.getClass()
        return model3D

    def transform(self, coordinate3D):
        model3D = VelocityModel3D()
        model3D.modelField = _FDtomoC.lib.transform3D(coordinate3D.coordinateField, self.modelField)
        model3D.coordinate.coordinateField = model3D.modelField.coordinate
        model3D.coordinate.mesh.meshField = model3D.modelField.coordinate.mesh
        model3D.coordinate.mesh.numberOfNode.pointField = model3D.modelField.coordinate.mesh.numberOfNode
        model3D.coordinate.origin.pointField = model3D.modelField.coordinate.origin
        model3D.coordinate.space.pointField = model3D.modelField.coordinate.space
        model3D.getClass()
        return model3D

    def makeNewModel(self, coordinate, vp_model, vs_model, perturbation, table_size, new_model_env):
        corField = coordinate.coordinateField

        vpModelFieldPtr = _FDtomoC.ffi.new("velocityModel3D *", vp_model.modelField)
        vsModelFieldPtr = _FDtomoC.ffi.new("velocityModel3D *", vs_model.modelField)

        perturbationField = perturbation.perturbationField

        makenewmodEnvField = new_model_env.makenewmodEnvField
        commonEnvField = new_model_env.commonEnv.commonEnvField

        _FDtomoC.lib.makenewmod(corField, vpModelFieldPtr, vsModelFieldPtr, perturbationField, table_size, makenewmodEnvField, commonEnvField)
        vp_model.modelField = vpModelFieldPtr[0]
        vs_model.modelField = vsModelFieldPtr[0]

    def getField(self):
        coodinateField = self.coordinate.getField()
        velocity = _FDtomoC.ffi.new("float[]", self.velocity)
        modelField = _FDtomoC.lib.createModel3D(coodinateField, velocity)

    def getClass(self):
        self.coordinate.getClass()
        size = self.coordinate.mesh.numberOfNode.x * self.coordinate.mesh.numberOfNode.y * self.coordinate.mesh.numberOfNode.z
        self.velocity = _FDtomoC.ffi.unpack(self.modelField.velocity, int(size))