# STFlow
* STFlow is the tool for seismic tomography that provides a high performance and abstraction of DSL. 

## How to download
```bash
# clone source code
cd <where you want FDtomoC to live>
git clone https://github.com/ncu-psl/STFlow.git

cd STFlow
```

## How to build
```bash
# GNU Compiler Collection
export CC=gcc

# Intel C Compiler
# export CC=icc

# build
# if you get Internal Compiler Error(ICE), try make without -j
bash build.sh
```

## How to use
```sh
cd demo/

# there exist three demos, you can execute the scripts in the folder of different examples.
# For example :
# cd small
# python demo_small.py

```
