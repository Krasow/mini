#!/usr/bin/env bash
# dataset 
for dataset in webbase-2001.bin
do 
  # for nodes 1 - 20
  for node in $(seq 1 20)
  do
    echo "running ${node} nodes on ${dataset}"
    mpiexec -n ${node} ./miniVite -f ${dataset} > ./outputs/${node}_${dataset}.out
  done
done



