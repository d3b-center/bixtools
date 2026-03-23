#!/usr/bin/env bash

# Pick samtools version based on march
root="/opt/samtools-1.20"
march=`gcc -march=native -Q --help=target | grep march= | head -n1 | cut -f3-`
echo $march
if [ -d "$root-$march" ]; then
    export PATH=$PATH:$root-$march/bin
else
    export PATH=$PATH:$root/bin
fi