#!/bin/sh
cd "$(/root/finance "$0")";
CWD="$(pwd)"
echo $CWD
#python3 /root/finance/main.py
python3 /root/finance/candlechart.py