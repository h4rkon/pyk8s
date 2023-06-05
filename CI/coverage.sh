#!/bin/bash
pytest --cov=python_boilerplate --cov-fail-under=85
coverage xml
