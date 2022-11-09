from typing import TextIO


def process(C: int, w: list[int]) -> list[int]:
    x=[-1]*len(w)
    ca=0
    peso_ca=0
    for i in range(len(w)):
        if peso_ca+w[i]<=C:
            x[i]=ca
            peso_ca+=w[i]
        else:
            ca+=1
            x[i]=ca
            peso_ca=w[i]
    return x



def read_data(f: TextIO) -> tuple[int, list[int]]:
    C= int(f.readline())
    w=[]
    for line in f:
        w.append(int(line))
    return C,w


def show_results(x: list[int]):
    for x_1 in x:
        print(x_1)


if __name__ == "__main__":
    C0, w0 = read_data()
    solucion = process(C0, w0)
    show_results(solucion)
