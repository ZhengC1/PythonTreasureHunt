#!usr/bin/python

def read_file(map_name):
    here = open(map_name, 'r')
    cat = here.readlines()
    cat = [w.replace(' ', '') for w in cat]
    print cat 
    here.close()
read_file('map2.txt')
