# -*- coding: utf-8 -*-
import pickle

file = open("Topic1 dataset/slangs.txt", 'r')
Lines = file.readlines()

empty = {}
for l in Lines:
    if l != "\n":
        sep = l.split("\t")
        sep[1] = sep[1].rstrip("\n")
        empty.update({sep[0]:sep[1]})
        
pickle.dump(empty, open("Dictionary.pkl","wb"))
