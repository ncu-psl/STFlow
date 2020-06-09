import sys
import os
path = os.getcwd()
sys.path.insert(1, path + "/../../")

from semanticModel  import coordinate, environment
from semanticModel.velocity_model import VelocityModel1D, VelocityModel3D
from semanticModel.mesh import Mesh1D, Mesh3D
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
