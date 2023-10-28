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
  fi
done < input
}

function sum {
  sum=0
  while read -r line; do
    sum=$((sum + line))
  done
  echo $sum
}

print_sums | sort -n | tail -n 1
print_sums | sort -n | tail -n 3 | sum
