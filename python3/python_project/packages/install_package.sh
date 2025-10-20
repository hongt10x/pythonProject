#!/bin/bash

for file_ in `ls *.whl`
do  
  echo $file_
  pip install $file_
done

