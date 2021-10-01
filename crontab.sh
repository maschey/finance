#!/bin/sh
cd "$(/root/finance "$0")";
CWD="$(pwd)"
echo $CWD
python3 main.py