#!usr/bin/python

class treasure_hunt(object):
    lines = [[0 for x in range(10)] for x in range(10)]
    with open("map.txt", "r") as treasure_map:
        lines = treasure_map.read().splitlines()
    print lines

    def backtrack(self, x, y, moves):
        if (x == 0 or x == 10) and (y == 0 or y == 10):
            return "found a solution %d %d Return it!" %(x, y)
        else:
            value = lines[x][y]
            possible_states = [
            for i in possible_states:
                is_success = backtrak(self


