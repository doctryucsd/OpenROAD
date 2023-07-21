from __future__ import annotations
import sys
from typing import List, Tuple, Dict
import multiprocessing as mp
import os


def get_files(dir: str) -> List[str]:
    files: List[str] = os.listdir(dir)
    files = sorted(files)
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


def read_tree(
    tree_file: str, points_idx: Dict[Tuple[int, int], int]
) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    stps: List[Tuple[int, int]] = []
    edges: List[Tuple[int, int]] = []

    num_terminals: int = len(points_idx)

    with open(tree_file, "r") as f:
        # terminals
        for _ in range(num_terminals):
            line = f.readline().split()
            assert len(line) == 3, line
            x: int = int(line[0])
            y: int = int(line[1])
            tgt: int = int(line[2])
            src: int = points_idx[(x, y)]
            edges.append((tgt, src))

        stp_id: int = num_terminals
        while line := f.readline().split():
            assert len(line) == 3, line
            x: int = int(line[0])
            y: int = int(line[1])
            tgt: int = int(line[2])
            src: int = stp_id
            stps.append((x, y))
            if tgt != src:
                edges.append((tgt, src))
            stp_id += 1

    return (stps, edges)


def get_result(
    point_file: str, tree_file: str
) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    points: List[Tuple[int, int]] = read_points(point_file)
    points_idx: Dict[Tuple[int, int], int] = {}

    for i, point in enumerate(points):
        points_idx[point] = i

    (stps, edges) = read_tree(tree_file, points_idx)

    return (stps, edges)


def worker(
    point_file: str, tree_file: str
) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    result: Tuple[List[Tuple[int, int]], List[Tuple[int, int]]] = get_result(
        point_file, tree_file
    )
    return result


def get_results(
    point_files: List[str], tree_files: List[str]
) -> List[Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]]:
    assert len(point_files) == len(tree_files), (len(point_files), len(tree_files))
    inputs: List[Tuple[str, str]] = [
        (point_file, tree_file)
        for (point_file, tree_file) in zip(point_files, tree_files)
    ]
    with mp.Pool() as pool:
        point_sets: List[
            Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]
        ] = pool.starmap(worker, inputs)
    return point_sets


def write_file(
    result: Tuple[List[Tuple[int, int]], List[Tuple[int, int]]], file_name: str
) -> None:
    (stps, edges) = result
    with open(file_name, "w") as f:
        f.write("steiner points\n")
        for stp in stps:
            (x, y) = stp
            f.write(f"{x} {y}\n")
        f.write("edges\n")
        for edge in edges:
            (src, tgt) = edge
            f.write(f"{src} {tgt}\n")


def write_results(
    results: List[Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]],
    files: List[str],
    output_dir: str,
) -> None:
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for result, file in zip(results, files):
        file_name: str = os.path.basename(file)
        write_file(result, os.path.join(output_dir, file_name))


def extract_num(file: str) -> int:
    assert len(file.split(".")) == 2
    return int(file.split(".")[0])


def main() -> None:
    points_dir: str = sys.argv[1]
    trees_dir: str = sys.argv[2]
    output_dir: str = sys.argv[3]

    point_files: List[str] = get_files(points_dir)

    tree_files: List[str] = os.listdir(trees_dir)
    tree_files = sorted(tree_files, key=extract_num)
    tree_files = [os.path.join(trees_dir, file) for file in tree_files]

    results: List[Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]] = get_results(
        point_files, tree_files
    )

    # get tree file names

    write_results(results, tree_files, output_dir)


if __name__ == "__main__":
    main()
