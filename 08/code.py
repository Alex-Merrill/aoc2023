import math
import os
import re


def solve1(dirs, graph, start, part2=False):
    # first solution
    curr = start
    d_i = 0
    steps = 0
    while True:
        steps += 1
        curr = graph[curr][dirs[d_i % len(dirs)]]

        if part2 and curr[2] == "Z":
            break
        elif not part2 and curr == "ZZZ":
            break

        d_i += 1

    return steps


def solve2(dirs, graph, start):
    """
    second solution:
    finds beginning of cycle, finds length from beginning of cycle to all end
    nodes on cycle, finds total cycle length.
    """
    curr = start
    d_i = 0
    steps = 0
    cycle_offset = 0
    visited = dict()
    visited[(curr, d_i % len(dirs))] = 0
    while True:
        steps += 1
        curr = graph[curr][dirs[d_i % len(dirs)]]
        d_i += 1

        if (curr, d_i % len(dirs)) in visited:
            cycle_offset = visited[(curr, d_i % len(dirs))]
            break

        visited[(curr, d_i % len(dirs))] = steps

    cycle_length = 0
    visited = set([(curr, d_i % len(dirs))])
    cyc_st_to_end_offsets = []
    while True:
        cycle_length += 1
        curr = graph[curr][dirs[d_i % len(dirs)]]
        d_i += 1

        if curr[2] == "Z":
            cyc_st_to_end_offsets.append(cycle_length)

        if (curr, d_i % len(dirs)) in visited:
            break

        visited.add((curr, d_i % len(dirs)))

    return cycle_offset, cyc_st_to_end_offsets, cycle_length


def make_graph(map):
    graph = dict()
    for connection in map:
        node, a, b = re.findall(r"\w+", connection)
        graph[node] = (a, b)

    return graph


def main():
    """
    This LCM solution shouldn't work for part 2 as there could be multiple
    "**Z" finish nodes for each start node, in which case it would really be
    the minimuma LCM of every combination of cycle lengths of each start node.
    ex:
        "**A" -> "***" -> "**Z" -> "**Z"
        "**A" -> "***" -> "***" -> "**Z"

    In this case, the minimum steps is 3, but using the LCM on the first

    """
    inpt = open(f"{os.path.dirname(__file__)}/input.txt").read().strip()
    dirs, graph = inpt.split("\n\n")
    dirs = [0 if c == "L" else 1 for c in dirs]
    graph = make_graph(graph.split("\n"))

    print("Part 1:")
    print(
        f"{solve1(dirs, graph, 'AAA')} steps are required to reach ZZZ from AAA"
    )
    print("------------------")

    mults = [
        solve1(dirs, graph, s, part2=True)
        for s in filter(lambda x: x[2] == "A", graph.keys())
    ]
    print("Part 2:")
    print(
        f"{math.lcm(*mults)} steps are required for all ghosts to sync up at an ending node"
    )
    print("------------------")

    """
    as we can see from the output of cycle_info below, a trivial LCM must exist
    if the length of the cycle is equal to the length of the offset from the
    starting node to the beginning of the cycle plus the length of the offset
    from the start of the cycle to the finish node. In this case, each starting
    node loops periodically with a period of the cycle length. If the offset of
    the starting node to the beginning of the cycle is not the complement of
    the cycle length and the offset of the start of the cycle to the finish
    node, then the first period (the length from the starting node to the
    finish node) is different from the subsequent periods of finish node to
    finish node.

    ex:
    start -> "***" -> cycle_start -> "***" -> finish
                           ^                    ↓ 
                           <-    <-     <-     <-

    the number of steps from the start node to the finish node is 4. However
    subsequent cycles have a period of 3. Thus the first cycle is offset by 1
    from the remaining cycles. Using some math and the extended euclidean
    algorithm the lcm of two numbers with a phase offset can be calculated
    if it exists. I leave the implementation of that as an exercise to the
    reader :)

    It's also possible the phase offset causes the periods to never synchronize
    with eachother, for example:

    start -> cycle_start -> finish
                  ^           ⇓
                  <-         <-

    start -> cycle_start -> *** -> finish -> ***
                  ^                           ⇓
                  <-       <-         <-     <-
    
    the first cycle has a period of 2 and offset of two, it hits the finish
    node on every even number. The second cycle has a period of 4 and offset
    3. Thus, it hits the finish node only on odd numbers. 
    """
    starts = [s for s in filter(lambda x: x[2] == "A", graph.keys())]
    cycle_info = []
    for s in starts:
        cycle_info.append(solve2(dirs, graph, s))

    print("Part 2(a):")
    print("Cycle info: ", cycle_info)
    print(
        f"{math.lcm(*map(lambda x: x[2], cycle_info))} steps are required for all ghosts to sync up at an ending node"
    )


main()
