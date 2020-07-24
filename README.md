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
STFlow在設計上，必須以TomographyBuilder()當作開頭，然後必需要依序呼叫method:
* Environment() 
* Event() 
* Station() 
* VelocityModel()
我們必須傳入給這些method，STFlow規定的元件，如下列程式碼:

```python
TomographyBuilder() \  
  .Environment(environment) \  
  .Event(event) \  
  .Station(station) \  
  .VelocityModel(velocitModel3D) \  
  .execute(mode = 'Seq', count = 1)   

```
而為了要讓STFlow更多的表達方式，我們希望一個method可以被替換成其它method。因此我們以元件間的相關性當作依據，判定一個method可不可以再進一步展開。舉例來說，速度模型(velocityModel)可以被座標(coordinate)及一維速度模型(velocityModel1D)建構而成，因此我們在使用上，VelocityModel()這個method就可以改寫成Coordinate()、ReferenceModel()。不過在使用上，我們仍然需要呼叫VelocityModel()，但是不需要給予他參數，而是給予Coordinate()、ReferenceModel()需要的資料(coordinate、velocityModel1D)即可，這樣是希望使用者可以知道這些method之間的關係，在撰寫上時如果發生錯誤，像是method的順序發生顛倒，相對容易發現錯誤的地方，如下列程式碼:

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
而具體的參數資料型態，請參考wiki的內容。

## Example :

```sh
cd demo/

# there exist three demos, you can execute the scripts in the folder of different examples.
# For example :
# cd small
# python demo_small.py

```
