#---This is an example of a specification file for running sphrayderv and 
#       associated programs
#
#       Variables are specified by inputing the variable name followed by the
#       value of that variable.
#
#       Blank lines and lines beginning with # are not read in and so may
#       be used for comments
#
#       Blanks and tabs are ignored
#
#       This file is read in and interpreted by the subroutine "parseparms"
#
#------Origin of the model in spherical system.  This lat (y0), lon (x0), depth (z0) specifies the location of the upper
#       NW corner of the grid.    120.2/120.8/22.75/23.25
        x0  121.30
        y0  24.30
        z0  -2.0

#------Fine grid spacing (dq, df, h).  h is the depth spacing in km, dq and df the latitude and longitude
#       spacing in degrees.  Note that if dq and df are not specified they will be computed
#      in the software to match h for the origin chosen.
		h   2.0

#------Coarse grid specifications
#  nxc, nyc, and nzc are the number of nodes in the x, y, and z directions
#  limit coarse: (151,151,33)  fine:(301,301,62)
nxc       22
nyc       42
nzc       22

igridx  2 2 2 1 1 1 1 1 1 1 \
        1 1 1 1 1 1 1 1 1 2 \
		2
		
		
igridy  2 2 1 1 1 1 1 1 1 1 \
		1 1 1 1 1 1 1 1 1 1 \
		1 1 1 1 1 1 1 1 1 1 \
		1 1 1 1 1 1 1 1 1 2 \
		2
      

igridz  2 \
        1 1 1 1 1 1 1 1 1 1 \
		2 2 2 2 2 2 2 2 4 4 \                            
#  Patterns used for checkerboard tests.  "perc" is the percentage perturbation. 
#  The pattern values multiply perc to give the total percent perturnbation in the
#  model.  Note that should be nxc values of ipatx, nyc values of ipaty, and nzc
#  values of ipatz in the tables below. (NOTE" ipatx = igridx + 1)

ipatx    1  1 -1 -1  1  1 -1 -1  1  1 \
         1  1 -1 -1  1  1 -1 -1  1  1 1
       
ipaty    1  1 -1 -1  1  1 -1 -1  1  1 \
         1  1 -1 -1  1  1 -1 -1  1  1 1

ipatz    1  1 -1 -1  1  1 -1 -1  1  1 \
        -1  1 -1  1 -1  1 -1  1 -1  1 \
        -1  1 -1  1 -1

perc       10.0

#------Lat/Lon Center of Coordinates geographic location of Cartesian (0,0)
#      Note this is not used in spherical coordinate system.
        clat   23.87
        clon  121.60

#  sph = 1 if we are using a spherical system, 0 for cartesian
        sph     1

#  flat = 1 to work with flattened earth (transform spherical <-> cartesian)
        flat    1

#  FDLOC VARIABLES
     nthres      50     #  Minimum number of phases allowed 
     resthres   3.0     #  Residual threshold (absolute time)
     resthrep   3.0     #  Residual threshold (percentage time)
     stdmax     3.0     #  Standard Deviation threshold

#  TELRAYDERV VARIABLES
      iray     0        # if = 1, write out raypaths to file
      iraystat 1        # if = 1, write out ray statistics to file
      idatout  1        # if = 1, write out new data file with residuals
      nomat    0        # if = 0, do inverse problem; = 1 no matrix output
      dmean    0        # if = 1, demean shot data (like solving for origin time).
      resflag  5.0      # minimum size of flagged residuals in output data file

#  GENERAL VARIABLES
      istacor   0       # if = 1, solve for station corrections
      ivpvs     1       # if = 0 for shear slowness; =1 vp/vs derivatives
      doshot    0       # if = 1, process shot data
      dotel     0       # if = 1, process teleseismic data
      normal    1       # if = 0, normalize the columns of A (mscale; now defunct) 
      havepo    0       # if = 1, use a Po file (FITGRAV). Assigned to iusepo.
      const     0       # assigned to "icon". if = 1, MSCALE adds constraints
      dmax    1.0       # Maximum correlation distance (addcovs and makecovs)
      iaddcon   0       # in addgrav and makepo, add more constraints if = 1.
      ipop      1       # if = 1, use P speeds only in adding Po constraints (addpo/makepo)
      ittnum    1       # Iteration counter used to number log files in several programs

# A matrix (partial derivative) scaling factors.
      hscale 10.0       # Hypocenter Scaling
      cscale 500.0      # Constraint Scaling (addcon)
      vscale  10        # Constraint Scaling (addcovs)
      gscale  0.1       # Gravity Scaling (addgravc)
      pscale  1.0       # Po Scaling (addpo)

# LSQR VARIABLES
      damper 500       # Like it sounds
      intlim 0          # Iteration limit. if = 0, use the default iteration limit 

# MAKENEWMOD VARIABLES
      mavx 3            #  Moving window length in x direction
      mavy 3            #  Moving window length in y direction
      mavz 3            #  Moving window length in z direction
      nsmooth 3         #  Number of times to smoothe

# TELFILT parameters
      kthres      4     #  Minimum number of teleseismic phases allowed
      avrthres 10.0     #  Maximum value for average residual
      resthret  3.0     #  Maximum residual

# SPHFDSYN parameters
      allsta      2     #  = 2 P&S waves at all stations in the station list.
                        #  = 1 P waves only at all stations in the station list.
                        #  = 0 to reproduce the stations in the input data file

##################################################################################
#
#                          ****FILE CONNECTIONS****
#
#       Note that for a normal iteration you will probably want to update
#       the following file names:
#
#       oldvfil => update to the last iteration model (often the previous fmodfil)
#       fdloc output (fsumfil, outlfil, fheadfil, fdatfil)
#       locdfil => should usually match fdatfil
#       telrerr, hitfile => save for post mortem testing
#       nmodfil => the new model from lsqr
#       fmodfil, modpfil, modsfil => new model from makenewmod
#
#       Typically I preserve the basename and increment the iteration number
#
#       The following files generally are changed every teleseismic only iteration:
#
#       oldvfil         lsqr_smooth.mod#-1      The current model
#       telrerr         rayderv.err#-1          Errors and statistics
#       nmodfil         lsqr.newmod#            New Perturbation File
#       timedir         ./ttimes#-1             Travel times for the current model
#       fmodfil         lsqr_smooth.mod#        New Model (P&S)
#               where "#" refers to the iteration number.  Thus, we should start
#               with 0's for the first 3 files and 1's for the last 2 and
#               we can automatically update the spec files 
#
#       
#
# Table for building the 1D model (make1d).  Output from make1d goes to oldvfil.
onedfil         ../data/HL_2km/CWB_mdl
# Output from the checker program; 
# checker.f uses the model in oldvfil as input and applies the pattern described above for perturbations
chkvfil         checker.mod

# Starting Coarse model file name (P and S)
oldvfil         CWB.mod

# Travel time directory
timedir         ../data/HL_2km/TTimes_HL001

#par file list
parlist         ../data/HL_2km/runsphfd.txt

#
# FDLOC Input
#
leqsfil         ../data/HL_2km/run_files/arrivals/hyp.Fdtomo171819  # Local Earthquake data - header input for sphfdsyn, sphfdloc
#
# FDLOC Output
#
fsumfil         fdloc.sumout1    #  Location Summary File
outlfil         fdloc.outliers1  #  Outliers
fhedfil         fdloc.nheads1    #  New Headers
fdatfil         local.data_re1   #  New Data - output from sphfdsyn also

#
# TELRAYDERV Input
#
locdfil         local.data_re1 # Local Earthquake Data : typically = fdatfil
shotfil         ../data/HL_2km/run_files/arrivals/all_shot.data      # Shot Data
telefil         ../data/HL_2km/run_files/arrivals/tele_01_09.dat    # Teleseismic Data
#telefax                tele.data 
#
# TELRAYDERV Output:  Errors and statistics
#
telrerr         rayderv.err           # Errors and statistics
hitfile         rayderv.hit           # Hit file (sphrayderv output)
#
# Note: These are input to makehyps as well.
dtdhfil         dtdh.out                # Hypo derivatives
bookfil         book.out                # Hypo bookkeeping
stcfile         stacor.out              # Station correction derivative file (if istcor = 1)
#
# Telrayderv conditional output (static)
#
raystat         sphrayderv.raystats   # Ray Stats file (if iraystat=1)
dotfile         sphrayderv.datout     # Synthetic Data output (idatout=1)
headfil         sphrayderv.hedout     # Synthetic Header Output (idatout=1)
entfile         sphrayderv.entries    # Entry points (nomat=1)
raypfil         sphrayderv.raypaths   # sphrayderv ray path output (iray=1)
#
# ADDPO/MAKEPO INPUT
#
mpofile         ./iasp.mod      # The Po Model

#
# MAKEPO OUTPUT
#
indfile         cndx.out        # Index File
mdatfil         cond.data       # Data Vector
mhitfil         makepo.hitfile  # Hit file
#
# MAKEPO OUTPUT/ADDCONS INPUT
# consfil       constraints.out         # Constraint matrix file
consfil         ../data/constraint.table        # Constraint table (borehole: addcon input)

# MSCALE OUTPUT
#
merrfil         mscale.err      # Error File

# Generic files:  These are used by many programs and are reset manually or
# in a shell file like runinvg or rungen.
dtdsfil         dtds.out        # Current A Matrix
resfile         res.out         # Current Data vector
bigafil         new.dtds        # New A Matrix
sdatfil         new.data        # New Data Vector
sclefil         index.file      # Current Index File

#
# FITGRAV INPUT FILES
#
gdatfil         ../data/park.selgrav    #  gravity data (bouguer anomalies)

#
# FITGRAV OUTPUT FILES
#
gmodfil         lsqr_t.mod      # New P&S Slowness Model
dgdsfil         grav.dgds       # dg/ds derivatives
finegrv         grav1           # Basename for density and predicted gravity files

#
# RUNF04/RUNLSQR OUTPUT FILES
#
nmodfil         lsqr.newmod1   # New Perturbation File
fresfil         lsqr_res.out  # Residuals

#
# MAKENEWMOD OUTPUT FILES
#
fmodfil         lsqr_smooth.mod1       # New Model (P&S)

# filter events from the tele data file
telfinf         ../data/HL_2km/runs_files/arrivals/tele_01_09.dat   # Teleseismic Data

# TELFILT OUTPUT FILES
#
tgodfil         tele_good.data  # Good data
tbadfil         tele_bad.data   # Bad data

#
#
# Static files:  Rarely if ever change during a run
#
stafile         ../data/HL_2km/run_files/HL171819.coords  # Station List
# stafile               relsta.coords   # Station List
#
# Fine model file name (P and S): Output from c2f
#
# Note: these names must be used for runinvg to work correctly (they
#       are hardwired in that script).
#
finevel         tempvel
finpvel         tempvel.pvel
finsvel         tempvel.svel

# c2f test grid output
tgrdfil         c2f.gridout

# Telrayderv P &S base travel times and ellipticity files (input)
pbasfil         ../data/HL_2km/runs_files/parameter/Ptimes.base293
#  NB:  We don't use S wave, so just repeat the P time file here
sbasfil         ../data/HL_2km/runs_files/parameter/Stimes.base293
elipfil         ../data/HL_2km/runs_files/parameter/elpcor

# Generic MSCALE output files for testing/plotting a posteriori
amapfil         amap.out        # Vector lengths of A columns

# Additional "Hard" constraints from borehole (for example)
aconfil         downhole.const


# Not specified because not used yet
#
# GRAVDERV OUTPUT
ghitfil         grav.hit1       # Gravderv hit map/output
gresfil         grav.res1       # Gravderv residual output
#

