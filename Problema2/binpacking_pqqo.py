from typing import TextIO


def process(C: int, w: list[int]) -> list[int]:
    x = [-1] * len(w)
    peso_contenedores = [0]
    indices = range(len(w))
    sorted_indices = sorted(indices, key=lambda i: -w[i])
    for i in sorted_indices:
        for nc in range(len(peso_contenedores)):
            if peso_contenedores[nc] + w[i] <= C:
                x[i] = nc
                peso_contenedores[nc] += w[i]
                break
        if x[i] == -1:  # else: si sale por break
            peso_contenedores.append(w[i])
            x[i] = len(peso_contenedores) - 1
    return x


def read_data(f: TextIO) -> tuple[int, list[int]]:
    C = int(f.readline())
    w = []
    for line in f:
        w.append(int(line))
    return C, w


def show_results(x: list[int]):
    for x_1 in x:
        print(x_1)


if __name__ == "__main__":
    C0, w0 = read_data()
    solucion = process(C0, w0)
    show_results(solucion)
