#!/usr/bin/env/python

class treasure_map(object):
#this opens the file with the "r" command
    treasure_map = open("map.txt", "r")
    cat = treasure_map.read()

#closes the file.
    treasure_map.close()

#prints the test out to the screen
    print cat[1][1]

treasure_map()
