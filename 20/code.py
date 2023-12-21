import os
from collections import deque
from math import lcm


def get_next_pulse(module, src_module, dest_module, pulse):
    if module[0] == "%":
        if pulse == "hi":
            return None
        module[1] = not module[1]
        return "hi" if module[1] else "lo"
    else:
        mod_mem = module[3]
        old_pulse = mod_mem[src_module]
        mod_mem[src_module] = pulse
        if pulse == "hi" and old_pulse == "lo":
            module[1] += 1
        elif pulse == "lo" and old_pulse == "hi":
            module[1] -= 1

        return "lo" if module[1] == len(mod_mem) else "hi"


def solve(
    signals,
    graph,
    part2=False,
    output_cond=None,
):
    signals = deque(signals)  # (src_mod, dest_mod, signal)
    count = [0, 0]
    output_cond_his = []
    while signals:
        src_module, dest_module, curr_pulse = signals.popleft()

        # add src_module to output if dest_module is our output condition
        if part2 and dest_module == output_cond and curr_pulse == "hi":
            output_cond_his.append(src_module)

        if curr_pulse == "lo":
            count[0] += 1
        else:
            count[1] += 1

        if dest_module not in graph:
            continue

        next_pulse = get_next_pulse(
            graph[dest_module], src_module, dest_module, curr_pulse
        )

        if not next_pulse:
            continue

        for next_module in graph[dest_module][2]:
            signals.append((dest_module, next_module, next_pulse))

    return count if not part2 else output_cond_his


def create_graph(lines):
    graph = {}  # module : [(%|&), (state|num hi), dest modules, (None|memory)]
    start = None
    for line in lines:
        module, dest = line.split(" -> ")

        if module == "broadcaster":
            start = dest.split(", ")
            start = list(
                zip(["broadcaster"] * len(start), start, ["lo"] * len(start))
            )
            continue

        if module[0] == "%":
            graph[module[1:]] = [module[0], False, dest.split(", "), None]
        else:
            graph[module[1:]] = [module[0], 0, dest.split(", "), {}]

    for k, v in graph.items():
        if v[0] != "&":
            continue

        for k1, v1 in graph.items():
            if k == k1:
                continue

            for mod in v1[2]:
                if mod == k:
                    v[3][k1] = "lo"

    return graph, start


def part1(lines):
    graph, start = create_graph(lines)
    total_lo = total_hi = 0
    for _ in range(1000):
        lo, hi = solve(start, graph)
        total_lo += lo
        total_hi += hi

    return total_lo * total_hi


def part2(lines):
    graph, start = create_graph(lines)
    output_cond = None
    output_mems = None
    for k, v in graph.items():
        if "rx" in v[2]:
            output_cond = k
            output_mems = {k: float("infinity") for k in v[3].keys()}

    assert output_cond is not None

    i = 0
    found = 0
    while found < len(output_mems):
        i += 1
        output_cond_his = solve(
            start,
            graph,
            part2=True,
            output_cond=output_cond,
        )

        if not output_cond_his:
            continue

        for src in output_cond_his:
            if output_mems[src] == float("infinity"):
                output_mems[src] = i
                found += 1

    return lcm(*output_mems.values())


def main():
    lines = open(f"{os.path.dirname(__file__)}/input.txt").read().strip().splitlines()

    print(f"part 1: {part1(lines)}")

    print(f"part 2: {part2(lines)}")


main()
