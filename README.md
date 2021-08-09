# STFlow
STFlow is a Python library for performing seismic tomography tasks. It provides a higher-level abstraction while supporting OpenMP and MPI modes. 

## How to download
```bash
# clone source code
cd <where you want STFlow to live>
git clone https://github.com/ncu-psl/STFlow.git

cd STFlow
```
## Dependencies
The following tools should be installed on the machine and available from the executable/library search path:
* gcc/icc compiler
* python interpreter
* cmake
* A functional MPI 1.x/2.x/3.x implementation like MPICH or Open MPI built with shared/dynamic libraries
* Needed python packages
  * CFFI
  * mpi4py


## Building
```bash
# GNU Compiler Collection
export CC=gcc

# Intel C Compiler
# export CC=icc

# build
# if you get Internal Compiler Error(ICE), try make without -j
bash build.sh

# For linking c libraries to python extension module, you'll need to add path of libraries to LD_LIBRARY_PATH.
# <path to STFlow> is where you want STFlow to exists. 
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:<<path to STFlow>>/build/lib/common
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:<<path to STFlow>>/build/lib/FDtomo

```

## How to use
The kernel of STFlow code is actually one line of code, for example:
```python
TomographyBuilder() \  
  .Environment(environment) \  
  .Event(event) \  
  .Station(station) \  
  .VelocityModel(velocitModel3D) \  
  .execute(mode = 'Seq', count = 1)   

```
A valid STFlow code should start with TomographyBuilder(), call the following methods in order, and finish with execute():
* Environment() 
* Event() 
* Station() 
* VelocityModel()

These method calls can be regarded as language elements describing a seismic tomography task with earthquake events and seismic stations.
An element may be further replaced with other elements according the semantics of STFlow, for example, the velocity model can be constructed by a coordinate system and a reference model as well:
```python
TomographyBuilder() \  
  .Environment(environment) \  
  .Event(event) \  
  .Station(station) \  
  .VelocityModel() \  
    .Coordinate(coordinate) \
    .ReferenceModel(velocityModel1D) \
  .execute(mode = 'Seq', count = 1)   

```
where VelocityModel(velocitModel3D) is replaced with Coordinate(coordinate) and ReferenceModel(velocityModel1D).
This design benefits from method chaining and the implementation of every method is checking the parameters rather than carrying out the computation; the task will not start before execute() is called. STFlow can be regarded as a domain-specific language embedded in Python.

Several examples we used in our experiments can be found in the demo folder. For the grammar and arguments, please refer to the wiki page.

## Example :

```sh
cd demo/

# there exist three demos, you can execute the scripts in the folder of different examples.
# For example :
# cd small
# python demo_small.py

```
