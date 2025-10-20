#!/bin/bash

echo 123
time=4
function good() {
    if [ $time -eq 1 ]; then
      echo "find you"
    fi
}
good

