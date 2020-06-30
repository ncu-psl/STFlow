import abc
from cffi import FFI
import _FDtomoC

class CommonEnv(object):
    def __init__(self):
        self.commonEnvField = None
        self.iread = None
        self.ivs = None
        self.vpvs = None
        self.istacor = None
        self.ivpvs = None
        self.doshot = None
        self.dotel = None
        self.normal = None
        self.havepo = None
        self.icon = None
        self.dmax = None
        self.iaddcon = None
        self.ipop = None
        self.ittnum = None

    def getClass(self):
        self.iread = self.commonEnvField.iread
        self.ivs = self.commonEnvField.ivs
        self.vpvs = self.commonEnvField.vpvs
        self.istacor = self.commonEnvField.istacor
        self.ivpvs = self.commonEnvField.ivpvs
        self.doshot = self.commonEnvField.doshot
        self.dotel = self.commonEnvField.dotel
        self.normal = self.commonEnvField.normal
        self.havepo = self.commonEnvField.havepo
        self.icon = self.commonEnvField.icon
        self.dmax = self.commonEnvField.dmax
        self.iaddcon = self.commonEnvField.iaddcon
        self.ipop = self.commonEnvField.ipop
        self.ittnum = self.commonEnvField.ittnum

    def getField(self):
        commonEnvFieldPtr = _FDtomoC.ffi.new("CommonEnv *", {'iread' : self.iread, 'ivs' : self.ivs, \
                                            'vpvs' : self.vpvs, 'istacor' : self.istacor, 'ivpvs' : self.ivpvs, \
                                            'doshot' : self.doshot, 'normal' : self.normal, 'havepo' : self.havepo, \
                                            'icon' : self.icon, 'dmax' : self.dmax, 'iaddcon' : self.iaddcon, \
                                            'ipop' : self.ipop, 'ittnum' : self.ittnum})
        return commonEnvFieldPtr[0]

class LocEnv(object):
    def __init__(self, commonEnv = None):
        self.commonEnv = commonEnv
        self.locEnvField = None
        self.iread = None
        self.ivs = None
        self.nthres = None
        self.kmin = None
        self.ndiv = None
        self.ndiv2 = None
        self.vpvs = None
        self.resthres = None
        self.resthrep = None
        self.stdmax = None        
        self.leqsfil = None
        self.fsumfil = None
        self.outlfil = None
        self.fhedfil = None
        self.fdatfil = None

    def create(self, file = None):
        if (file != None):
            tmp = _FDtomoC.ffi.new("char[]", file.encode('ascii'))
            commonEnv = CommonEnv()
            loc_env = LocEnv(commonEnv)
            loc_env.locEnvField = _FDtomoC.lib.setLocEnv(tmp)
            loc_env.commonEnv.commonEnvField = _FDtomoC.lib.setCommonEnv(tmp)
            loc_env.getClass()
            return loc_env

    def getClass(self):
        self.iread = self.locEnvField.iread
        self.ivs = self.locEnvField.ivs
        self.nthres = self.locEnvField.nthres
        self.kmin = self.locEnvField.kmin
        self.ndiv = self.locEnvField.ndiv
        self.ndiv2 = self.locEnvField.ndiv2
        self.vpvs = self.locEnvField.vpvs
        self.resthres = self.locEnvField.resthres
        self.resthrep = self.locEnvField.resthrep
        self.stdmax = self.locEnvField.stdmax
        self.leqsfil = _FDtomoC.ffi.string(self.locEnvField.leqsfil)
        self.fsumfil = _FDtomoC.ffi.string(self.locEnvField.fsumfil)
        self.outlfil = _FDtomoC.ffi.string(self.locEnvField.outlfil)
        self.fhedfil = _FDtomoC.ffi.string(self.locEnvField.fhedfil)
        self.fdatfil = _FDtomoC.ffi.string(self.locEnvField.fdatfil)
        self.commonEnv.getClass()


    def getField(self):
        locEnvFieldPtr = _FDtomoC.ffi.new("LocEnv *", {'iread' : self.iread, 'ivs' : self.ivs, \
                                                          'nthres' : self.nthres, 'kmin' : self.kmin, \
                                                          'ndiv' : self.ndiv, 'ndiv2' : self.ndiv2, \
                                                          'vpvs' : self.vpvs, 'resthres' : self.resthres, \
                                                          'resthrep' : self.resthrep, 'stdmax' : self.stdmax, \
                                                          'leqsfil' : self.leqsfil, 'fsumfil' : self.fsumfil, \
                                                          'outlfil' : self.outlfil, 'fhedfil' : self.fhedfil, \
                                                          'fdatfil' : self.fdatfil}) 
        return locEnvFieldPtr[0]

class SphraydervEnv(object):
    def __init__(self, commonEnv = None):
        self.sphraydervEnvField = None
        self.commonEnv = commonEnv
        self.iray = None
        self.iraystat = None
        self.idatout = None
        self.nomat = None
        self.dmean = None
        self.kmin = None
        self.kmax = None
        self.ido1d = None
        self.locdfil = None
        self.telrerr = None
    	self.dtdsfil = None 
        self.resfile = None
        self.hitfile = None 
        self.dtdhfil = None
        self.bookfil = None 
        self.sclefil = None
        self.telefil = None
        self.pbasfil = None
        self.sbasfil = None
        self.shotfil = None
        self.elipfil = None
        self.raystat = None
        self.dotfile = None
        self.headfil = None
        self.entfile = None
        self.stcfile = None 
        self.specfile = None

    def create(self, file = None):
        if (file != None):
            tmp = _FDtomoC.ffi.new("char[]", file.encode('ascii'))
            commonEnv = CommonEnv()
            sphrayderv_env = SphraydervEnv(commonEnv)
            sphrayderv_env.sphraydervEnvField = _FDtomoC.lib.setSphraydervEnv(tmp)
            sphrayderv_env.commonEnv.commonEnvField = _FDtomoC.lib.setCommonEnv(tmp)
            sphrayderv_env.getClass()
            return sphrayderv_env


    def getClass(self):
        self.iray = self.sphraydervEnvField.iray
        self.iraystat = self.sphraydervEnvField.iraystat
        self.idatout = self.sphraydervEnvField.idatout
        self.nomat = self.sphraydervEnvField.nomat
        self.dmean = self.sphraydervEnvField.dmean
        self.kmin = self.sphraydervEnvField.kmin
        self.kmax = self.sphraydervEnvField.kmax
        self.ido1d = self.sphraydervEnvField.ido1d
        self.locdfil = _FDtomoC.ffi.string(self.sphraydervEnvField.locdfil)
        self.telrerr = _FDtomoC.ffi.string(self.sphraydervEnvField.telrerr)
    	self.dtdsfil = _FDtomoC.ffi.string(self.sphraydervEnvField.dtdsfil) 
        self.resfile = _FDtomoC.ffi.string(self.sphraydervEnvField.resfile)
        self.hitfile = _FDtomoC.ffi.string(self.sphraydervEnvField.hitfile)
        self.dtdhfil = _FDtomoC.ffi.string(self.sphraydervEnvField.dtdhfil)
        self.bookfil = _FDtomoC.ffi.string(self.sphraydervEnvField.bookfil) 
        self.sclefil = _FDtomoC.ffi.string(self.sphraydervEnvField.sclefil)
        self.telefil = _FDtomoC.ffi.string(self.sphraydervEnvField.telefil)
        self.pbasfil = _FDtomoC.ffi.string(self.sphraydervEnvField.pbasfil)
        self.sbasfil = _FDtomoC.ffi.string(self.sphraydervEnvField.sbasfil)
        self.shotfil = _FDtomoC.ffi.string(self.sphraydervEnvField.shotfil)
        self.elipfil = _FDtomoC.ffi.string(self.sphraydervEnvField.elipfil)
        self.raystat = _FDtomoC.ffi.string(self.sphraydervEnvField.raystat)
        self.dotfile = _FDtomoC.ffi.string(self.sphraydervEnvField.dotfile)
        self.headfil = _FDtomoC.ffi.string(self.sphraydervEnvField.headfil)
        self.entfile = _FDtomoC.ffi.string(self.sphraydervEnvField.entfile)
        self.stcfile = _FDtomoC.ffi.string(self.sphraydervEnvField.stcfile)
        self.specfile = _FDtomoC.ffi.string((self.sphraydervEnvField.specfile))
        self.commonEnv.getClass()


    def getField(self):
        sphraydervEnvFieldPtr = _FDtomoC.ffi.new("SphraydervEnv *", {'iray' : self.iray, 'iraystat' : self.iraystat, \
                                           'idatout' : self.idatout, 'nomat' : self.nomat, 'dmean' : self.dmean, \
                                           'kmin' : self.kmin, 'kmax' : self.kmax, 'ido1d' : self.ido1d, \
                                           'locdfil' : self.locdfil, 'telrerr' : self.telrerr, 'dtdsfil' : self.dtdsfil, \
                                           'resfile' : self.resfile, 'hitfile' : self.hitfile, 'dtdhfil' : self.dtdhfil, \
                                           'bookfil' : self.bookfil, 'sclefil' : self.sclefil, 'telefil' : self.telefil, \
                                           'pbasfil' : self.pbasfil, 'sbasfil' : self.sbasfil, 'shotfil' : self.shotfil, \
                                           'elipfil' : self.elipfil, 'raystat' : self.raystat, 'dotfile' : self.dotfile, \
                                           'headfil' : self.headfil, 'entfile' : self.entfile, 'stcfile' : self.stcfile, \
                                           'specfile' : self.specfile}) 
        
        return sphraydervEnvFieldPtr[0]




class RunlsqrEnv(object):
    def __init__(self, commonEnv = None):
        self.runlsqrEnvField = None
        self.commonEnv = commonEnv
        self.intlim = None
        self.damper = None
        self.nmodfil = None
        self.fresfil = None

    def create(self, file = None):
        if (file != None):
            runlsqr_env = RunlsqrEnv()
            tmp = _FDtomoC.ffi.new("char[]", file.encode('ascii'))
            commonEnv = CommonEnv()
            runlsqr_env = RunlsqrEnv(commonEnv)
            runlsqr_env.runlsqrEnvField = _FDtomoC.lib.setRunlsqrEnv(tmp)
            runlsqr_env.commonEnv.commonEnvField = _FDtomoC.lib.setCommonEnv(tmp)
            runlsqr_env.getClass()
            return runlsqr_env

    def getClass(self):
        self.intlim =  self.runlsqrEnvField.intlim
        self.damper =  self.runlsqrEnvField.damper
        self.nmodfil =   _FDtomoC.ffi.string(self.runlsqrEnvField.nmodfil)
        self.fresfil =   _FDtomoC.ffi.string(self.runlsqrEnvField.fresfil)
        self.commonEnv.getClass()

    def getField(self):
        runlsqrEnvFieldPtr = _FDtomoC.ffi.new("RunlsqrEnv *", {'intlim' : self.intlim, 'damper' : self.damper, \
                                                            'nmodfil' : self.nmodfil, 'fresfil': self.fresfil})
        return runlsqrEnvFieldPtr[0]

class MakenewmodEnv(CommonEnv):
    def __init__(self, commonEnv = None):
        self.makenewmodEnvField = None
        self.commonEnv = commonEnv
        self.mavx = None 
        self.mavy = None
        self.mavz = None
        self.nsmooth = None
        self.limitu = None
        self.ipscflg = None
        self.ido1d = None
        self.dvperc = None
        self.pertscl = None

    def create(self, file = None):
        if (file != None):
            tmp = _FDtomoC.ffi.new("char[]", file.encode('ascii'))
            commonEnv = CommonEnv()
            makenewmod_env = MakenewmodEnv(commonEnv)
            makenewmod_env.makenewmodEnvField = _FDtomoC.lib.setMakeNewmodEnv(tmp)
            makenewmod_env.commonEnv.commonEnvField = _FDtomoC.lib.setCommonEnv(tmp)
            makenewmod_env.getClass()
            return makenewmod_env

    def getClass(self):
        self.mavx = self.makenewmodEnvField.mavx 
        self.mavy = self.makenewmodEnvField.mavy
        self.mavz = self.makenewmodEnvField.mavz
        self.nsmooth = self.makenewmodEnvField.nsmooth
        self.limitu = self.makenewmodEnvField.limitu
        self.ipscflg = self.makenewmodEnvField.ipscflg
        self.ido1d = self.makenewmodEnvField.ido1d
        self.dvperc = self.makenewmodEnvField.dvperc
        self.pertscl = self.makenewmodEnvField.pertscl
        self.commonEnv.getClass()

    def getField(self):
        makenewmodEnvFieldPtr = _FDtomoC.ffi.new("MakenewmodEnv *", {'mavx' : self.mavx, 'mavy' : self.mavy, \
                                                'mavz' : self.mavz, 'nsmooth' : self.nsmooth, 'limitu' : self.limitu, \
                                                'ipscflg' : self.ipscflg, 'ido1d' : self.ido1d, 'dvperc' : self.dvperc, \
                                                'pertscl' : self.pertscl})
