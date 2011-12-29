#!/bin/bash

source env/bin/activate
make model_info 2> $(date +'%Y-%m-%d').dat 1> /dev/null

