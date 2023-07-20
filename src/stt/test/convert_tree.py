from __future__ import annotations
import sys
from typing import List, Tuple
import multiprocessing as mp
import os


def get_files(dir: str) -> List[str]:
    files: List[str] = os.listdir(dir)
    files = [os.path.join(dir, file) for file in files]

    return files


def read_points(file: str) -> List[Tuple[int, int]]:
    ret: List[Tuple[int, int]] = []
    with open(file, "r") as f:
        while line := f.readline().split():
            assert len(line) == 2, line
            x: int = int(line[0])
            y: int = int(line[1])
            query: Tuple[int, int] = (x, y)
            if query not in ret:
                ret.append((x, y))
    return ret


def worker(file: str) -> List[Tuple[int, int]]:
    points: List[Tuple[int, int]] = read_points(file)
    return points


def get_results(dir: str) -> List[List[Tuple[int, int]]]:
    files: List[str] = get_files(dir)
    with mp.Pool() as pool:
        point_sets: List[List[Tuple[int, int]]] = pool.map(worker, files)
    return point_sets


def write_file(point_sets: List[List[Tuple[int, int]]], file_name: str) -> None:
    with open(file_name, "w") as f:
        for i, net in enumerate(point_sets):
            f.write(f"Net net_{i} 0\n")
            for j, point in enumerate(net):
                f.write(f"point_{i}_{j} {point[0]} {point[1]}\n")
            f.write("\n")


def write_results(
    results: List[Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]],
    files: List[str],
    output_dir: str,
) -> None:
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for result, file in zip(results, files):
        write_file(result, os.path.join(output_dir, file))


def main() -> None:
    points_dir: str = sys.argv[1]
    trees_dir: str = sys.argv[2]
    output_dir: str = sys.argv[3]
    
    

    results: List[Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]] = get_results(
        points_dir, trees_dir
    )

    # get tree file names

    write_file(results, point_files, output_dir)


if __name__ == "__main__":
    main()
