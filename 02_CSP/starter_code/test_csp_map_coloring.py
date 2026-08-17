"""
Tests for csp_map_coloring.py

Run with:
    pytest 02_CSP/starter_code/test_csp_map_coloring.py -v

`test_given_example` below is COMPLETE -- study it as a template.

You must then write the 3 required test cases (test_case_1, test_case_2,
test_case_3). Read ../../03_Test_Case_Design/mindmap.md and
training_guide.md before choosing what your 3 cases should cover. Aim to
pick 3 *different* categories rather than 3 variations of the same thing
(e.g. one typical/solvable case, one edge/boundary case, one
unsolvable/over-constrained case).

For each test case, write a short comment explaining WHICH category from
the mind-map it represents and WHY you chose it.
"""
import pytest
from csp_map_coloring import (
    VARIABLES,
    NEIGHBOURS,
    DOMAIN,
    backtracking_search,
    is_consistent,
)


def _is_valid_solution(solution, variables, neighbours):
    """Helper: check a solution assigns every variable and breaks no
    adjacency constraint. Already implemented -- reuse this in your tests.
    """
    if solution is None:
        return False
    if set(solution.keys()) != set(variables):
        return False
    for var, value in solution.items():
        for neighbour in neighbours[var]:
            if neighbour in solution and solution[neighbour] == value:
                return False
    return True


# ---------------------------------------------------------------------
# GIVEN EXAMPLE -- complete, do not modify. Use this as your template.
# Category: typical/normal small solvable case (from the mind-map:
# "Solvability -> solvable case").
# ---------------------------------------------------------------------
def test_given_example():
    solution = backtracking_search(VARIABLES, DOMAIN)

    assert solution is not None
    assert _is_valid_solution(solution, VARIABLES, NEIGHBOURS)


# ---------------------------------------------------------------------
# TODO Test Case 1
# Mind-map Category: Graph Topology & Solution Validity -> Full Constraint Verification
# Why: Verifies that every single adjacent pair of regions in the solved map
# strictly receives different colors.
# ---------------------------------------------------------------------
def test_case_1():
    solution = backtracking_search(VARIABLES, DOMAIN)
    assert solution is not None
    
    # Explicitly check every neighbor relationship in Australia map
    for var in VARIABLES:
        for neighbour in NEIGHBOURS[var]:
            assert solution[var] != solution[neighbour]


# ---------------------------------------------------------------------
# TODO Test Case 2
# Mind-map Category: Domain & Solvability -> Unsolvable / Over-constrained Case
# Why: Restricting the available domain to only 2 colors makes coloring 
# Australia impossible (it chromatic number is 3), testing solver failure handling.
# ---------------------------------------------------------------------
def test_case_2():
    restricted_domain = ["Red", "Green"]
    solution = backtracking_search(VARIABLES, restricted_domain)
    assert solution is None


# ---------------------------------------------------------------------
# TODO Test Case 3
# Mind-map Category: Edge Cases -> Unconstrained / Disconnected Nodes
# Why: Tests handling of isolated graph nodes like Tasmania ('T'), ensuring it 
# receives a valid color and can be freely reassigned without causing conflicts.
# ---------------------------------------------------------------------
def test_case_3():
    solution = backtracking_search(VARIABLES, DOMAIN)
    assert solution is not None
    assert solution["T"] in DOMAIN
    
    # Tasmania has no neighbors, changing its color must remain consistent
    test_assignment = solution.copy()
    test_assignment["T"] = "Blue"
    assert is_consistent(test_assignment, "T", "Blue")


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))