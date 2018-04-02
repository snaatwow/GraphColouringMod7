import graph_io
import sys
from GreedyColoring import *


def writedotgraph(graph):
    print("writing")
    with open('mygraph.dot', 'w') as j:
        graph_io.write_dot(graph, j)


def testGraphdesc(file_location):
    with open(file_location) as f:
        G = graph_io.load_graph(f)

        print("Graph " + str(file_location))
        desc = sortDesc(G)
        greedyG, chromaticnr, time = Greedy(G, desc)
        print("chromaticnumber descending order =" + str(chromaticnr) + " time elapsed: " + str(time))
    return chromaticnr, time


def testGraphasc(file_location):
    with open(file_location) as f:
        G = graph_io.load_graph(f)

        asc = sortAsc(G)
        greedyG, chromaticnr, time = Greedy(G, asc)
    writedotgraph(greedyG)
    print("chromaticnumber ascending order =" + str(chromaticnr) + " time elapsed: " + str(time))
    return chromaticnr, time

def testGraphrndm(file_location):
    with open(file_location) as f:
        G = graph_io.load_graph(f)


        random = shuffle(G)
        greedyG, chromaticnr, time = Greedy(G, random)
    print("chromaticnumber random order =" + str(chromaticnr) + " time elapsed: " + str(time))
    writedotgraph(greedyG)
    return chromaticnr, time

def testrandom(file_location):
    min = 10000000
    besttime = 100000

    for i in range(1, 100, +1):
        cnr, time = testGraphrndm((file_location))
        if (cnr < min):
            min = cnr
        if time < besttime:
            besttime = time



    print("minimum chromatic nr: "+ str(min))
    print("besttime: " + str(besttime))


if __name__ == '__main__':
    testGraphdesc("Graphs//randomplanar10.gr")