#!/bin/bash
path1='data/access_log_20180324-124435.log'
path2='filtered-data.txt'

python main.py --input $path1 --ouptut $path2

exit 0
