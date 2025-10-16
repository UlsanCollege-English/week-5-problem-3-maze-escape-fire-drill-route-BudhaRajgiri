# src/maze.py
from collections import deque
from typing import List, Tuple, Optional

def find_path(grid: List[List[int]],
              start: Tuple[int, int],
              end: Tuple[int, int],
              debug: bool = False) -> Optional[List[Tuple[int, int]]]:
    """
    BFS shortest path in a 4-connected grid.
    - grid: list of lists (0=open, non-zero=wall)
    - start/end: (row, col)
    - Returns list[(r,c)] path or None.
    - debug=True prints step-by-step diagnostics.
    """
    # Basic validation
    if not isinstance(grid, list) or len(grid) == 0:
        if debug: print("invalid grid (not list or empty)")
        return None
    if not all(isinstance(row, list) for row in grid):
        if debug: print("invalid grid (rows not all lists)")
        return None

    rows = len(grid)
    cols = len(grid[0])
    if any(len(row) != cols for row in grid):
        if debug: print("invalid grid (ragged rows)")
        return None

    # Validate start/end
    try:
        sr, sc = start
        er, ec = end
    except Exception:
        if debug: print("start/end should be 2-tuples")
        return None
    if not all(isinstance(x, int) for x in (sr, sc, er, ec)):
        if debug: print("start/end coordinates must be ints")
        return None

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    if not in_bounds(sr, sc) or not in_bounds(er, ec):
        if debug: print("start or end out of bounds", start, end)
        return None

    # treat any non-zero as wall
    try:
        if grid[sr][sc] != 0 or grid[er][ec] != 0:
            if debug: print("start or end is blocked")
            return None
    except Exception as e:
        if debug: print("error indexing grid:", e)
        return None

    if start == end:
        return [start]

    q = deque([start])
    parent = {start: None}
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    if debug: print("BFS begin from", start, "to", end)
    while q:
        r, c = q.popleft()
        if debug: print("visit", (r, c))
        if (r, c) == end:
            # reconstruct
            path = []
            cur = end
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            path = path[::-1]
            if debug: print("path found:", path)
            return path

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc) and (nr, nc) not in parent:
                try:
                    if grid[nr][nc] == 0:
                        parent[(nr, nc)] = (r, c)
                        q.append((nr, nc))
                        if debug: print(" enqueue", (nr, nc))
                except Exception as e:
                    if debug: print("skipping bad cell", nr, nc, e)

    if debug: print("no path found")
    return None
