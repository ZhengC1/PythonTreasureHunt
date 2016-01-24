#!usr/bin/env/python

class treasure_map(object):
    #this opens the file with the "r" command
    lines = [[0 for x in range(10)] for x in range(10)]
    x = 5
    y = 5
    input = ""
    def read_into_array(self):
        with open("map.txt", "r") as treasure_map:
            lines = treasure_map.read().splitlines()

    def start_game(self):
        if (x == 0 or x == 10) and (y == 0 or y == 10):
            cat = x + " " + y
            return cat 




cat = treasure_map()
cat.read_into_array()
