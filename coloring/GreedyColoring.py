from graph import *
import random
import time



def sortAsc(Graph):

    vertices = []
    for v in Graph.vertices:
        vertices.append((v, v.degree))

    output = sorted(vertices, key=lambda tup: tup[1])

    output = [(a) for a, b in output]


    return output

def sortDesc(Graph):

    vertices = []
    for v in Graph.vertices:
        vertices.append((v, v.degree))

    output = sorted(vertices, key=lambda tup: tup[1], reverse = True)

    output = [(a) for a, b in output]


    return output

def shuffle(Graph):
    toshuffle = []
    for v in Graph.vertices:
        toshuffle.append(v)

    random.shuffle(toshuffle)
    return toshuffle




def Greedy(Graph, list):
    # give all vertices color -1

    start = time.time()

    if list == None:
        vertices = Graph.vertices
    else: vertices = list

    chromaticnr = 0
    firstavailable = -1

    for v in vertices:
        v.label = -1

    # make a list with available colours and set availability to true
    colours = [True] * len(Graph.vertices)


    #set colour of first vertex in list to 0
    vertices[0].label = 0

    """Checks for every graph if it has neighbours, and if so:
    it sets the colour of a neighbour to unavailable, so it cannot be used for this vertex"""
    for i in vertices:
        neighbours = i.neighbours

        if len(neighbours) != 0:
            for j in range(0, len(neighbours), 1):
                if neighbours[j].label != -1:
                    colours[neighbours[j].label] = False



        for c in range(0, len(colours), 1):

            if colours[c] == True:
                firstavailable = c
                if firstavailable > chromaticnr:
                    chromaticnr = firstavailable
                break

        i.label = firstavailable

        for i in range(0, len(colours), 1):
            colours[i] = True


    chromaticnr = chromaticnr + 1

    end = time.time()
    timer = end - start

    return Graph, chromaticnr, timer


