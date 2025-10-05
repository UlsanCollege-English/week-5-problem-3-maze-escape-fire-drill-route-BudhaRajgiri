[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_JC3Htkz)
# Maze Escape — Fire Drill Route

## Story
Your building is running a fire drill. You have a floor plan grid where `0` is passable and `1` is a wall. Starting from `S`, can you reach `E`? If so, return **one** path as a list of `(row, col)` cells.

## Technical Description
Write:

```py
find_path(grid, start, end) -> list | None
```
- grid: list of lists of ints (0/1)

- start, end: (r, c) tuples within bounds

- Return a path including start and end, or None if unreachable.

- Movement: up/down/left/right only.

- Use recursion with backtracking.

## Hints
- Base case: start == end → return [end].

- Mark visited to avoid cycles.

- Try neighbors; on success, prepend current cell.

## Run Tests Locally
```bash
python -m pytest -q
```
## Common Problems
- Forgetting to mark visited before recursing → loops.

- Returning an empty list instead of None for no path.

- Going diagonal (not allowed here).
