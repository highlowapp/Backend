#!/bin/bash
set -u -e -o pipefail

# ./start_docker.py writes '<ip_address>:<db port>' to stdout
IFS=\; read -a ip_port <<<"`./start_docker.py`"
ip="${ip_port[0]}"
port="${ip_port[1]}"

./quicknotes -local -verbose -db-host ${ip} -db-port ${port} $@