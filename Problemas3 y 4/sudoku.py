from __future__ import annotations  # Utilizar clase ante de definirlo
import sys
from copy import deepcopy
from dataclasses import dataclass
from typing import TextIO
from sudoku_lib import *  # importa todas funciones de sudoku.lib
from algoritmia.schemes.bt_scheme import DecisionSequence, bt_solve
from collections.abc import Iterator


# Position = tuple[int, int]  #(row,col)
# Sudoku = list[list[int]]

def read_data(f: TextIO) -> Sudoku:
    return desde_cadenas(f.readlines())  # f.readlines() leer todas lineas
    # cadenas=[]
    # for line in f: #f.readline
    #    cadenas.append(line)
    # return desde_cadenas(cadenas)


def show_results(sudokus: Iterator[Sudoku]):
    for sudoku in sudokus:
        pretty_print(sudoku)


def process_nair(sudoku: Sudoku) -> Iterator[Sudoku]:
    @dataclass
    class Extra:
        sudoku: Sudoku

    class SudokuDS(DecisionSequence):
        def is_solution(self) -> bool:
            return primera_vacia(self.extra.sudoku) is None

        def successors(self) -> Iterator[SudokuDS]:
            pos = primera_vacia(self.extra.sudoku)
            if pos is not None:
                r, c = pos
                for num in posibles_en(self.extra.sudoku, pos):
                    # sudoku2 = self.extra.sudoku # en lista, asignación "=" es hacer referencia a otro, solo hace referencia a sudoku padre
                    # sudoku2 = self.extra.sudoku[:] # aunque la matriz no es misma, pero su cada fila sigue hace referencia a su padre
                    # sudoku2 = [linea[:] for linea in self.extra.sudoku] # hacer un acopia de la matriz, cambia una no afecta a otra
                    # sudoku2 = deepcopy(self.extra.sudoku)  # O bien utiliza copy.deepcopy
                    sudoku2 = [linea[:] for linea in self.extra.sudoku]  # más eficiecia
                    sudoku2[r][c] = num
                    yield self.add_decision(num, Extra(sudoku2))

        def solution(self) -> Sudoku:
            return self.extra.sudoku

    initial_ds = SudokuDS(Extra(sudoku))
    return bt_solve(initial_ds)


def process_fast(sudoku: Sudoku) -> Iterator[Sudoku]:
    @dataclass
    class Extra:
        sudoku: Sudoku
        vacias: set[Position]

    class SudokuDS(DecisionSequence):
        def is_solution(self) -> bool:
            return len(self.extra.vacias) == 0

        def successors(self) -> Iterator[SudokuDS]:
            best_posibles = None
            pos = (-1, -1)
            for pos_v in self.extra.vacias:
                aux = posibles_en(self.extra.sudoku, pos_v)
                if best_posibles is None or len(aux) < len(best_posibles):
                    best_posibles= aux
                    pos = pos_v

            if pos is not None:
                r, c = pos
                for num in posibles_en(self.extra.sudoku, pos):
                    sudoku2 = [linea[:] for linea in self.extra.sudoku]  # si no hace copia va más eficiecia
                    sudoku2[r][c] = num
                    vacias2 = set(self.extra.vacias)
                    vacias2.remove(pos)
                    yield self.add_decision(num, Extra(sudoku2, vacias2))

        def solution(self) -> Sudoku:
            return self.extra.sudoku

    initial_ds = SudokuDS(Extra(sudoku, set(vacias(sudoku))))
    return bt_solve(initial_ds)


process = process_fast

if __name__ == "__main__":
    sudoku0 = read_data(sys.stdin)
    sudokus0 = process(sudoku0)
    show_results(sudokus0)
