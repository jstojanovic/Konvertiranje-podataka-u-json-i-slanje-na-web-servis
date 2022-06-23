#!/usr/bin/env python3
import os
import json
import requests

directory = "./"

dictionari = {}
listt = []
data = []
for filename in  os.listdir(directory):
    feedback = open(os.path.join(directory, filename), 'r')
    for line in feedback:
        listt.append(line)
    dictionari['title'] = listt[0].strip('\n')
    dictionari['name'] = listt[1].strip('\n')
    dictionari['date'] = listt[2].strip('\n')
    dictionari['feedback'] = listt[3].strip('\n')
    listt = []
    print(requests.post("http://34.121.188.87/feedback/", json=dictionari))
