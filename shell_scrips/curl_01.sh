#!/bin/bash                                                                                                                                                                                     
CURL='/usr/bin/curl'
RVMHTTP="https://raw.github.com/wayneeseguin/rvm/master/binscripts/rvm-installer"
CURLARGS="-f -s -S -k"

# you can store the result in a variable
raw="$($CURL $CURLARGS $RVMHTTP)"

# or you can redirect it into a file:
$CURL $CURLARGS $RVMHTTP > /tmp/rvm-installer