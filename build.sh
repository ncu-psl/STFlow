#!/bin/bash

mkdir build
cd build
cmake ..
make -j # it will generate needed c libraries for STFlow

cd ../semanticModel
python bindToPython.py #generate python extension module for STFlow
