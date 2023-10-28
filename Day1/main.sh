#!/bin/bash

function print_sums {
sum=0
best=0

while read -r line; do
  if [[ -z $line ]]; then
    echo $sum
    sum=0
  else
    sum=$((sum + line))
    #echo $line, $sum
  fi
done < input
}

print_sums | sort -n | tail -n 1
