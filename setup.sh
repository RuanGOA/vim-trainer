#!/bin/sh

if ! $(which python3) -eq "python3 not found" ;
then 
  sudo install apt install python3.8
fi

if ! $(which pip3) -eq "pip3 not found" ;
then 
  sudo apt install python3-pip
fi

pip3 install -r requirements.txt

