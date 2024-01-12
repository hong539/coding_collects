#!/bin/bash

{
    echo "This is a sample line 1"
    echo "This is a sample line 2"
    echo "This is a sample line 3"
} | awk '{ print strftime("%Y/%m/%d %H:%M:%S"), $0 }' >> ./test.log