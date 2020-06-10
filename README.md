# STFlow
* STFlow is the tool for seismic tomography that provides a high performance and abstraction of DSL. 

## How to download
```bash
# clone source code
cd <where you want STFlow to live>
git clone https://github.com/ncu-psl/STFlow.git

cd STFlow
```
## Dependencies
The following tools should be installed and available on the machine executable / library search path:
* gcc/icc compiler
* python interpreter
* cmake
* A functional MPI 1.x/2.x/3.x implementation like MPICH or Open MPI built with shared/dynamic libraries.
* Needed python packages.
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
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:<<path to STFlow>>/build/lib/common
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:<<path to STFlow>>/build/lib/FDtomo

```

## How to use
```sh
cd demo/

# there exist three demos, you can execute the scripts in the folder of different examples.
# For example :
# cd small
# python demo_small.py

```
