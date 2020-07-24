import sys
import os
path = os.getcwd()
sys.path.insert(1, path + "/../../")

from semanticModel  import coordinate, environment
from semanticModel.velocity_model import VelocityModel1D, VelocityModel3D
from semanticModel.mesh import Mesh1D, Mesh3D
from semanticModel.coordinate import Coordinate1D, Coordinate3D
from semanticModel.station import Station
from semanticModel.event import Event
from semanticModel.point import PointDouble
from DSL.tomography import TomographyBuilder

file_path = "small.spec"
model1D_path = "TW_m30_mdl"
stafile = "stationloc_out.txt"
leqsfil = "All.txt"

loc_env = environment.LocEnv().create(file = file_path)
sphrayderv_env = environment.SphraydervEnv().create(file = file_path)
runlsqr_env = environment.RunlsqrEnv().create(file = file_path)
makenewmod_env = environment.MakenewmodEnv().create(file = file_path)

environment = {'loc_env' : loc_env, 'sphrayderv_env' : sphrayderv_env, 'runlsqr_env' : runlsqr_env, 'makenewmod_env' : makenewmod_env}
coarseMesh3D = Mesh3D().create(file = file_path)
fineMesh3D = coarseMesh3D.generateFineMesh()
event = Event().createArray(leqsfil)
station = Station().createArray(file = stafile)

vpModel = VelocityModel1D()
vsModel = VelocityModel1D()
VelocityModel1D().setVelocityModel(model1D_path, vpModel, vsModel)
origin = PointDouble(120.90, 23.80, -4.0)
space = PointDouble(2.0,2.0,2.0)
numberOfNode = int(coarseMesh3D.numberOfNode.z)
gridz = coarseMesh3D.gridz
zSpace = space.z
zOrigin = origin.z
coarseMesh1D = Mesh1D().create(numberOfNode = numberOfNode, grid = gridz)
cooarseCoordinate1D = Coordinate1D().create(coarseMesh1D, zSpace, zOrigin)
coarseVpModel1D = vpModel.transform(cooarseCoordinate1D)
coarseVsModel1D = vsModel.transform(cooarseCoordinate1D)
coarseCoordinate3D = Coordinate3D().create(coarseMesh3D, space, origin)
CoarseVpModel3D = VelocityModel3D().create(coarseCoordinate3D, coarseVpModel1D)
CoarseVsModel3D = VelocityModel3D().create(coarseCoordinate3D, coarseVsModel1D)
fineCoordinate3D = Coordinate3D().create(fineMesh3D, space, origin)
fineVpModel3D = CoarseVpModel3D.transform(fineCoordinate3D)
fineVsModel3D = CoarseVsModel3D.transform(fineCoordinate3D)


TomographyBuilder() \
    .Environment(environment) \
    .Event(event) \
    .Station(station) \
    .VelocityModel(CoarseVpModel3D, CoarseVsModel3D, fineVpModel3D, fineVsModel3D) \
    .execute(mode = 'Omp', count = 1) 


'''
TomographyBuilder() \
    .Environment(environment) \
    .Event(event) \
    .Station(station) \
    .VelocityModel() \
        .Coordinate(coarseCoordinate3D, fineCoordinate3D) \
        .ReferenceModel(vpModel, vsModel) \
    .execute(mode = 'Omp', count = 1) 

'''

'''
TomographyBuilder() \
    .Environment(environment) \
    .Event(event) \
    .Station(station) \
    .VelocityModel() \
        .Coordinate() \
            .Mesh(coarseMesh3D, fineMesh3D) \
            .Origin(origin) \
            .Space(PointDouble(2,2,2)) \
        .ReferenceModel(vpModel, vsModel) \
    .execute(mode = 'Omp', count = 1) 
'''