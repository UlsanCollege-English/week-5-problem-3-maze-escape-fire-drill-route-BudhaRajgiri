from src.maze import find_path

# ---- Normal (4) ----
def test_trivial_start_is_end():
    g = [[0]]
    assert find_path(g, (0,0), (0,0)) == [(0,0)]

def test_simple_straight_line():
    g = [[0,0,0]]
    p = find_path(g, (0,0), (0,2))
    assert p[0] == (0,0) and p[-1] == (0,2) and len(p) == 3

def test_simple_turn():
    g = [
        [0,1,0],
        [0,1,0],
        [0,0,0]
    ]
    p = find_path(g, (0,0), (2,2))
    assert p[0] == (0,0) and p[-1] == (2,2)

def test_open_grid_small():
    g = [
        [0,0],
        [0,0]
    ]
    p = find_path(g, (0,0), (1,1))
    assert p and p[0] == (0,0) and p[-1] == (1,1)

# ---- Edge (3) ----
def test_blocked_start():
    g = [[1,0],[0,0]]
    assert find_path(g, (0,0), (1,1)) is None

def test_blocked_end():
    g = [[0,0],[0,1]]
    assert find_path(g, (0,0), (1,1)) is None

def test_out_of_bounds():
    g = [[0]]
    assert find_path(g, (0,0), (0,1)) is None

# ---- Complex (3) ----
def test_no_path_maze():
    g = [
        [0,1,0,0],
        [0,1,0,1],
        [0,1,0,1],
        [0,1,0,1],
    ]
    assert find_path(g, (0,0), (3,2)) is None

def test_large_open_grid_diag_distance():
    n = 10
    g = [[0]*n for _ in range(n)]
    p = find_path(g, (0,0), (n-1,n-1))
    assert p[0] == (0,0) and p[-1] == (n-1,n-1) and len(p) >= 2*n-1

def test_snake_corridor():
    g = [
        [0,0,0,0],
        [1,1,1,0],
        [0,0,0,0],
        [0,1,1,1],
        [0,0,0,0],
    ]
    p = find_path(g, (0,0), (4,3))
    assert p and p[0] == (0,0) and p[-1] == (4,3)
