import graph_io
import sys
from GreedyColoring import *



def writedotgraph(graph):
    print("writing")
    with open('mygraph.dot', 'w') as j:
        graph_io.write_dot(graph, j)


def testGraph(file_location):
    with open(file_location) as f:
        G = graph_io.load_graph(f)

        print("Graph " + str(file_location))
        desc = sortDesc(G)
        greedyG, chromaticnr = Greedy(G, desc)

        print("chromaticnumber descending order =" + str(chromaticnr))

        asc = sortAsc(G)
        greedyG, chromaticnr = Greedy(G, desc)

        print("chromaticnumber ascending order =" + str(chromaticnr))

        random = shuffle(G)
        greedyG, chromaticnr = Greedy(G, desc)
        print("chromaticnumber random order =" + str(chromaticnr))

        writedotgraph(greedyG)

if __name__ == '__main__':

    #testGraph("Graphs//bbf200.gr")
    #testGraph("Graphs//WDE100.gr")
    #testGraph("Graphs//Graph1000.gr")
    testGraph(("Graphs//randomplanar10.gr"))
    testGraph(("Graphs//randomplanar10.gr"))
    testGraph(("Graphs//randomplanar10.gr"))
    testGraph(("Graphs//randomplanar10.gr"))
    testGraph(("Graphs//randomplanar10.gr"))
    testGraph(("Graphs//randomplanar10.gr"))