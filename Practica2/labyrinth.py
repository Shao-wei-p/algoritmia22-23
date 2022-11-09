from random import shuffle
import sys
from typing import TextIO

from algoritmia.datastructures.graphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet

Vertex = tuple[int, int]
Edge = tuple[Vertex, Vertex]


def read_data(f: TextIO) -> tuple[int, int]:
    rows = int(f.readline())
    cols = int(f.readline())
    return rows, cols


def create_labyrinth(rows: int, cols: int) -> UndirectedGraph:
    vertices: list[Vertex] = []
    for r in range(rows):
        for c in range(cols):
            vertices.append((r, c))
    mfs = MergeFindSet()
    for v in vertices:
        mfs.add(v)
    edges: list[Edge] = []
    for r, c in vertices:
        if r - 1 >= 0:
            e: Edge = ((r - 1, c), (r, c))
            edges.append(e)
        if c - 1 >= 0:
            e: Edge = ((r, c - 1), (r, c))
            edges.append(e)
    shuffle(edges)
    corridors: list[Edge] = []
    for e in edges:
        u, v = e
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            corridors.append(e)
    return UndirectedGraph(E=corridors)



def show_results(labyrinth: UndirectedGraph):
    print(labyrinth)


if __name__ == "__main__":
    rows2, cols2 = read_data(sys.stdin)
    labyrinth2 = create_labyrinth(rows2, cols2)
    show_results(labyrinth2)
