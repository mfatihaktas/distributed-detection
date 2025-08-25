#!/bin/bash

PY=python3


if [ $1 = "i" ]; then
  pip install -e .

elif [ $1 = "s" ]; then
  $PY scripts/sim_detection_center.py

elif [ $1 = "?" ]; then
  echo

else
  echo "Unexpected arg= $1"
fi
