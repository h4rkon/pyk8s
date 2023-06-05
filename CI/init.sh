#!/bin/bash
pip uninstall -y -r <(pip freeze) 
pip install -r requirements.txt
