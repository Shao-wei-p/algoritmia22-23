import sys
from random import shuffle

from algoritmia.datastructures.graphs import UndirectedGraph
from typing import TextIO

from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.queues import Fifo

Vertex = tuple[int, int]
Edge = tuple[Vertex, Vertex]
Path = list[Vertex]

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
def bf_search(g: UndirectedGraph[Vertex],
              source: Vertex,
              target: Vertex) -> list[Edge]:
    res = []
    queue: Fifo[Edge] = Fifo()
    seen: set[Vertex] = set()
    queue.push((source, source))  # arista fantasma
    seen.add(source)
    while len(queue) > 0:
        u, v = queue.pop()
        # yield u, v
        res.append((u, v))
        if v == target:
            return res
        for suc in g.succs(v):
            if suc not in seen:
                queue.push((v, suc))
                seen.add(suc)
    return []  # si no lo encintra pues devuelve lista vacía


def path_recover(edges: list[Edge],
                 target: Vertex) -> list[Vertex]:
    # construir diccionario bp
    bp = {}  # diccionario
    for e in edges:
        u, v = e
        bp[v] = u  # el padre de v es u
    # recuperar el camino deste target(while)
    path = [target]
    v = target
    while v != bp[v]:
        v = bp[v]
        path.append(v)

    return path
    #while:
     #   v2 = bp[v]
     #   path.append(v2)
      #  if v2 == v:
       #     break
        #v = v2


def read_data(f: TextIO) -> tuple[int, int]:
    rows = int(f.readline())
    cols = int(f.readline())
    return rows, cols


def process(rows: int, cols: int) -> tuple[UndirectedGraph[Vertex], Path]:
    g = create_labyrinth(rows, cols)
    edges = bf_search(g, (0, 0), (rows - 1, cols - 1))
    shortest_path = path_recover(edges, (rows - 1, cols - 1))
    return g, shortest_path


def show_results(path: Path):
    for v in path:
        print(v)


if __name__ == "__main__":
    rows0, cols0 = read_data(sys.stdin)  # evitar conflicto entre variable local y variable global
    graph0, path0 = process(rows0, cols0)
    show_results(path0)
