#!/bin/sh
source /usr/lib/openfoam/openfoam/etc/bashrc
cp ../propeller.stl ./constant/triSurface
blockMesh
surfaceFeatureExtract
snappyHexMesh -overwrite
createPatch -overwrite
python3 ./change_boundary.py
topoSet
setFields
simpleFoam 
python3 ./result.py
