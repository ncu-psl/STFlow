import abc
from cffi import FFI
from point import PointDouble
import _FDtomoC

class Station(object):
    def __init__(self):
        self.name = None
        self.location = PointDouble()
        self.stationField = None
        self.tmp = None

    def create(self, name = None, location = None):
        station = Station(name, location)
        locationField = _FDtomoC.ffi.new("Point3DDouble *", location)
        nameField = _FDtomoC.ffi.new("char[]", name)
        stationField = _FDtomoC.ffi.new("Station *", {'name' : nameField, 'location' : locationField})
        station.stationField = stationField
        return station

    def createArray(self, station = None, file = None):
        if(file != None):
            filename = _FDtomoC.ffi.new("char[]", file.encode('ascii'))
            stationField_list = _FDtomoC.lib.createStationList(filename, 1)
            stationField_array = _FDtomoC.lib.StationList2Arr(stationField_list)

            stationSize = _FDtomoC.lib.getStationCount(stationField_list)
            tmp = _FDtomoC.ffi.unpack(stationField_array, stationSize)

            station_array = []
            for i in tmp:
                new_station = Station()
                new_station.stationField = i
                new_station.location.pointField = i.location
                new_station.getClass()
                station_array.append(new_station)
            
            return station_array

    def getClass(self):
        self.name = _FDtomoC.ffi.string(self.stationField.name)
        self.location.getClass()

    def getField(self):
        self.tmp = {'name': _FDtomoC.ffi.new("char[]", self.name)}
        locationField = self.location.getField()
        stationFieldPtr = _FDtomoC.ffi.new("Station *", {'name' : self.tmp['name'], 'location' : locationField})
        return stationFieldPtr[0]