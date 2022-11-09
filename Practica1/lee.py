import sys
from typing import TextIO

def read_data(f: TextIO) -> list[int]:
# En l tenemos una cadena por línea:
    lines: list[str] = f.readlines()
# Transformamos cada línea en un entero:
    return [int(line) for line in lines]
#ints = []    ampliando del comando arriba
#for line in lines:
#ints.append(int(line))
#return ints
#squares = [x*x for x in range(1, n)] --> 1,4,9,16...

def show_results(nums: list[int]):
# Recorremos las listas con el bucle for
    for num in nums:
        print(num)


if __name__ == "__main__":
    nums = read_data(sys.stdin)
    show_results(nums)