#!/bin/bash

if [ "$1" = "-f" ]; then
   git clean -Xdf
else
    git clean -Xdfn
    while true; do
        read -p "Do you wish to delete the above? [n] " yn
        case $yn in
            [Yy]* ) git clean -Xdf; break;;
            [Nn]* ) exit;;
            * ) exit;;
        esac
    done
fi
