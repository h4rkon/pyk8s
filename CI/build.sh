#!/bin/bash

rm -rf build dist *.egg-info
python -m pep517.build .