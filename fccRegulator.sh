#!/bin/sh

# setup
mypath=$( python3 setup.py )
#echo $mypath

audiofile=$1
echo $audiofile

i=0
# loop!
while true;
do 
    echo $i
    # chop audio into 10 seconds
    chopping=$( python3 chopAudio.py $mypath $i $audiofile )
    echo $chopping
    if [[ "$chopping"='DONE' ]]
    then
        break
    endif

    # transcribe and write into csv
    $( python3 readAudio.py $mypath $i )

    # check for bad words
    $( python3 pySerial.py $mypath $i )

    # send to arduino

    $i=$i+1

done