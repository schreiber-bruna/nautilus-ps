#!/bin/bash
hostname=$(hostname)
echo Bem vindo $USER no pc $hostname
curl wttr.in/?0
touch ~/.welcome.data
echo "$(date)" >> ~/.welcome.data
