#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    # Your code here
    bp = {
        'Value': 0, 'Chosen': []
    }

    cap = 0
    for i in range(len(items)):
        if cap < capacity:
            bp['Value'] += items[i].value
            bp['Chosen'].append(items[i].index)

            cap += items[i].size
        else:
            return bp
            


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')
