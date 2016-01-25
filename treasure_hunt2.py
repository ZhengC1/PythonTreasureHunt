#!usr/bin/python

class treasure_hunt2(object):

    def __init__(self, map_file):
        self.lines = [[0 for x in  range(10)] for x in range(10)]
        self.table = [[1 for x in range(10)] for x in range(10)]
        with open(map_file, "r") as treasure_map:
            self.lines = treasure_map.read().splitlines()
        print self.lines

    def backtrack(self, x, y, moves):

        if self.table[x][y] == 0:
            return False

       value = int(self.lines[x][y])
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
        if (x + value) < 11 and (x + value) > -1:
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
        self.table[x][y] = 0
        return False

file_name = raw_input("name of file :")

cat = treasure_hunt2(file_name)

print cat.backtrack(5, 5, "")
print cat.table
