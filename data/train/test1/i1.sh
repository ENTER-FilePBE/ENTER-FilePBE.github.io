#!/usr/bin/env bash

low=2012
high=2015

i=$low

while [ "$i" -lt "$high" ]
do
    j=1
    while [ "$j" -lt "13" ]
    do
        k=1
        while [ "$k" -lt "21" ]
        do
            name=${i}"-"${j}"-"${k}".png"
            touch $name
            k=$(($k + 1))
        done
        j=$(($j + 1))
    done
    i=$(($i + 1))
done
