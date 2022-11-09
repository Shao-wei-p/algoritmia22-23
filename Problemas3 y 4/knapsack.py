from __future__ import annotations  # Utilizar clase ante de definirlo
import sys
from typing import TextIO, Iterator
from algoritmia.schemes.bt_scheme import ScoredDecisionSequence, bt_max_solve, Score

Weight = int
Value = int
Decision = int  # 0 o 1
Decisions = tuple[Decision, ...]  # una longitud dinámica


def read_data(f: TextIO) -> tuple[Weight, list[Value], list[Weight]]:
    capacity = int(f.readline())
    values = []
    weights = []
    for line in f:  # f.readline
        value_txt, weight_txt = line.strip().split()  # strip() sirve para limpiar el silabo que situa en el principio y en final
        values.append(int(value_txt))
        weights.append(int(weight_txt))
    return capacity, values, weights


def show_results(value: Value, weight: Weight, decisions: Decisions):
    print(value)
    print(weight)
    print(' '.join(str(d) for d in decisions))
    # for decision in decisions: #l=lista de cadena --> '#'.join(l)
    # print(decision)


def process(capacity: Weight,
            values: list[Value],
            weights: list[Weight]) -> tuple[Value, Weight, Decisions]:
    class Extra:
        current_weight: Weight

    class KnapsackDS(ScoredDecisionSequence):
        def is_solution(self) -> bool:
            return len(self) == len(values)

        def successors(self) -> Iterator[KnapsackDS]:  # cada paso puede tener dos posibilidad: si cabe 1; si no 0
            # si padre (1,1) es válido, su hijo (1,1,0) obviamente que es válido
            # pero su otro hijo (1,1,1) no sabemos que es valido o no, debe comprobar que cabe o no
            n = len(self)
            if n < len(values):
                if self.extra.current_weight + weights[n] <= capacity:
                    current_weight2 = self.extra.current_weight + weights[n]
                    yield self.add_decision(1, Extra(current_weight2))
                yield self.add_decision(0, self.extra)

        def solution(self) -> tuple[Value, Weight, Decisions]:
            return ..., self.extra.current_weight, self.decisions()

        def state(self):
            return len(self), self.extra.current_weight

        def score(self) -> Score:
            pass

    initial_ds = KnapsackDS()
    best_sol = list(bt_max_solve(initial_ds))[
        -1]  # normalmente debe vigilar si es vacía, pero en nuestro caso no hace falta
    return best_sol


if __name__ == "__main__":
    capacity0, values0, weights0 = read_data(sys.stdin)
    value0, weight0, decisions0 = process(capacity0, values0, weights0)
    show_results(value0, weight0, decisions0)
