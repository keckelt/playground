#!/bin/bash

file="./old_ip.txt"

if [ ! -f  $file ]
  then
    echo Create file to store IP: $file
    curl --silent ifconfig.me > $file; 
fi

OLD_IP=`head -n 1 $file`
echo Old IP is: $OLD_IP
PUBLIC_IP=`curl --silent ifconfig.me`
echo New IP is: $PUBLIC_IP

if [ "$OLD_IP" != "$PUBLIC_IP" ]
  then
    echo Update $file
    echo $PUBLIC_IP > $file
fi 

