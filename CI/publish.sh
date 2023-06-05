#!/bin/bash

bumpversion patch
docker build -t h4rkon/pyk8s:`cat VERSION` .
docker tag h4rkon/pyk8s:`cat VERSION` h4rkon/pyk8s:latest
docker push h4rkon/pyk8s:`cat VERSION`
docker push h4rkon/pyk8s:latest