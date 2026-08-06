"""
Tests for astar_grid.py

Run with:
    pytest 01_Informed_Search_A_Star/starter_code/test_astar_grid.py -v

`test_given_example` below is COMPLETE -- study it as a template.

You must then write the 3 required test cases (test_case_1, test_case_2,
test_case_3). Read ../../03_Test_Case_Design/mindmap.md and
training_guide.md before choosing what your 3 cases should cover. Aim to
pick 3 *different* categories (e.g. one typical/normal case, one
edge/boundary case, one unsolvable-or-stress case) rather than 3 variations
of the same thing.

For each test case, write a short comment explaining WHICH category from
the mind-map it represents and WHY you chose it.
"""
import pytest
from astar_grid import astar, heuristic, neighbours, find_cell


# ---------------------------------------------------------------------
# GIVEN EXAMPLE -- complete, do not modify. Use this as your template.
# Category: typical/normal small case (from the mind-map: "Structure ->
# straightforward, no obstacles").
# ---------------------------------------------------------------------
def test_given_example():
    grid = [
        "S..",
        "...",
        "..G",
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is not None
    assert path[0] == start
    assert path[-1] == goal
    # Shortest possible Manhattan path on an open 3x3 grid is 4 moves.
    assert cost == 4


# ---------------------------------------------------------------------
# Test Case 1
# Mind-map category: Solvability -> No valid path / Unsolvable
# Why: Verifies that A* correctly handles an unreachable goal and returns
# (None, float('inf')) when completely blocked by walls.
# ---------------------------------------------------------------------
def test_case_1():
    grid = [
        "S..#.",
        "...#G",
        "...#.",
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is None
    assert cost == float("inf")


# ---------------------------------------------------------------------
# Test Case 2
# Mind-map category: Grid & Node Positions -> Start equals Goal
# Why: Boundary edge case testing zero-distance behavior when the start
# cell is identical to the goal cell.
# ---------------------------------------------------------------------
def test_case_2():
    grid = [
        "S",
    ]
    start = (0, 0)
    goal = (0, 0)

    path, cost = astar(grid, start, goal)

    assert path == [(0, 0)]
    assert cost == 0


# ---------------------------------------------------------------------
# Test Case 3
# Mind-map category: Obstacles & Walls -> Forced detour / Wall barrier
# Why: Tests pathfinding around a vertical wall barrier to ensure A*
# finds the optimal detour path around obstacles.
# ---------------------------------------------------------------------
def test_case_3():
    grid = [
        "S#G",
        ".#.",
        "...",
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is not None
    assert path[0] == start
    assert path[-1] == goal
    assert cost == 6


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))