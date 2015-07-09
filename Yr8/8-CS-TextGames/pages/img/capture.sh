#!/bin/bash
# A simple bash script to screen capture
#
# Supply two arguments, the window id and number of captures

let x=1

# loop until it has captured the number of captures requested
while [ "$x" -le "$2" ]
do
  import -window $1 "capture$x.miff"
  # uncomment the line below
  # if you want more time in between screen captures
  sleep 0.1 
  let x+=1
done
