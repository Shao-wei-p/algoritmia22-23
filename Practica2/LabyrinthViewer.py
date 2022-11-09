from algoritmia.viewers.labyrinth_viewer import LabyrinthViewer
from labyrinth import create_labyrinth
if __name__ == "__main__":
    rows = int(input("Filas: "))
    cols = int(input("Columnas: "))
    labyrinth = create_labyrinth(rows, cols)
    lv = LabyrinthViewer(labyrinth, canvas_width=10 * cols, canvas_height=10 * rows, wall_width=1)
    lv.run()