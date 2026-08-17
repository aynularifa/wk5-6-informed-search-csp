# Implementation Notes & Reflection

## Heuristic Admissibility
The Manhattan and Euclidean distance heuristics used in the A* grid search are admissible because they compute straight-line or grid distance assuming an open field with zero obstacles. Because real grid obstacles can only force the path to take extra turns or steps, the heuristic $h(n)$ never overestimates the actual minimum remaining cost to reach the goal.

## Test Case Coverage Justification
Across both exercises, test cases cover distinct categories from the mind-map:
* **Grid Search Cases**: Tested complete obstacle blockades (unsolvable grids), zero-distance edge cases (start equals goal), and multi-obstacle pathfinding.
* **CSP Cases**: Tested complete map constraint validity, domain starvation (attempting to color Australia with only 2 colors), and unconstrained/isolated nodes (Tasmania).