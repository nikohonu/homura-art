#!/bin/bash
files=`ls homura_art/ui/*.ui`
for file in $files
do
   pyside6-uic "${file%%.*}".ui -g python -o "${file%%.*}".py
done