import random
import math


class Model:
    def __init__(self):
        self.allNodes = []
        self.customers = []
        self.matrix = []
        self.matrix_profit = []
        self.capacity = -1

    def BuildModel(self):
        random.seed(1)
        depot = Node(0, 50, 50, 0, 0)
        self.allNodes.append(depot)

        self.capacity = 150
        totalCustomers = 300

        for i in range (0, totalCustomers):
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            Servicetime = random.randint(5, 10)
            Profit = random.randint(5, 20)
            cust = Node(i + 1, x, y, Servicetime, Profit)
            self.allNodes.append(cust)
            self.customers.append(cust)

        rows = len(self.allNodes)
        self.matrix = [[0.0 for x in range(rows)] for y in range(rows)]
        self.matrix_profit = [[0.0 for x in range(rows)] for y in range(rows)]

        for i in range(0, len(self.allNodes)):
            for j in range(0, len(self.allNodes)):
                a = self.allNodes[i]
                b = self.allNodes[j]
                dist = ((a.x - b.x)**2 + (a.y - b.y)**2)**(1/2)
                self.matrix[i][j] = dist
                if a == b:
                    ratio = -2
                else:
                    ratio = round(b.profit / (b.time + dist),4)
                self.matrix_profit[i][j] = ratio


class Node:
    def __init__(self, idd, xx, yy, time, profit):
        self.x = xx
        self.y = yy
        self.ID = idd
        self.time = time
        self.profit = profit
        self.isRouted = False

class Route:
    def __init__(self, dp, cap, cost = 0, profit = 0):
        self.sequenceOfNodes = []
        self.sequenceOfNodes.append(dp)
        #self.sequenceOfNodes.append(dp)
        self.cost = cost
        self.capacity = cap
        #self.load = 0 #?
        self.profit = profit