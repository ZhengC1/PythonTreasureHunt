#!usr/bin/python

#Author: Chun Zheng
#Assignment: Backtracking Treasure Hunt
#Lang - python 2.7
#Class - Artificial Intelligence

class treasure_hunt(object):
    #reads maps that are 11 by 11
    def __init__(self, map_file):
        self.lines = [[0 for x in  range(10)] for x in range(10)]
        self.table = [[1 for x in range(10)] for x in range(10)]
        with open(map_file, "r") as treasure_map:
            self.lines = treasure_map.read().splitlines()
        print self.lines

    #the recursive function call to solve the map given.
    def backtrack(self, x, y, moves):

        if self.table[x][y] == 0:
            return False

        value = int(self.lines[x][y])
        print value
        if (x == 0 or x == 10) and (y == 0 or y == 10):
            print "found a solution %d %d Return it!" %(x, y)
            return True
        if (x - value) > -1 and (x - value) < 11:
            print "current position %d %d %s" %(x, y, moves)
            print "try moving up %d spaces" %value
            if self.backtrack(x - value, y, moves + " up"):
                print 'found a solution at %d %d. Return it!' %(x, y)
                return True
            else:
                self.table[x][y] = 0
        if (x + value) > -1 and (x + value) < 11:
            print "current position %d %d %s" %(x, y, moves)
            print "try moving down %d spaces" %value
            if self.backtrack(x + value, y, moves + " down"):
                print 'found a solution at %d %d, Return it!' %(x, y)
                return True
            else:
                self.table[x][y] = 0
        if (y - value) > -1 and (y - value) < 11:
            print "current position %d %d %s" %(x, y, moves)
            print "try moving left %d spaces" %value
            if self.backtrack(x, y - value, moves + " left"):
                print 'found a solution at %d %d, Return it!' %(x, y)
                return True
            else:
                self.table[x][y] = 0
        if (y + value) > -1 and (y + value) < 11:
            print "current position %d %d %s" %(x, y, moves)
            print "try moving right %d spaces" %value
            if self.backtrack(x, y + value, moves + " right"):
                print 'found a solution at %d %d, Return it!' %(x, y)
                return True
            else:
                self.table[x][y] = 0
        return False

#prints and asks what file you would like
file_name = raw_input("name of file :")

solution = treasure_hunt(file_name)

print solution.backtrack(5, 5, "")
