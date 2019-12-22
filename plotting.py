# -*- coding: utf-8 -*-

import ast
import pandas as pd

with open('connections.txt', 'r') as f:
    names = f.read()
connections = ast.literal_eval(names)
edges = set()
pairs = []
for pair in connections.items():
    pairs.append(pair)
for i in range(len(pairs)):
    for j in range(i + 1, len(pairs)):
        if pairs[i][0] in pairs[j][1]:
             print(pairs[i][0] + ' ' + pairs[j][0])
             edges.add((pairs[i][0], pairs[j][0]))
print(edges)
