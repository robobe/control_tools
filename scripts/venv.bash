#!/bin/bash
set -e

: ' 
check if venv exist (venv folder)
if not create

if exists
    source it
    intstall all requirements
'

if [ ! -d "venv" ]
then
    python3 -m venv venv
fi

source venv/bin/activate
pip install -r requirements-dev.txt
