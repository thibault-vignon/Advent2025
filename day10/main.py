import networkx as nx
import pyomo.environ as pyo
from pyomo.opt import check_available_solvers

def factory_buttons_switches(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        linecount = 0
        ops_count = 0
        for line in lines:
            final_buttons = line.split('[')[1].split(']')[0]
            n_buttons = len(final_buttons)
            print(f"Line {linecount} has {n_buttons} buttons")
            goal = 0
            for idx in range(n_buttons):
                if final_buttons[idx] == '#':
                    goal ^= 1 << idx
            G = nx.Graph()
            G.add_nodes_from(range(0, 2**n_buttons))
            ops = line.split(']')[1].split('{')[0].strip().split(' ')
            for op in ops:
                switches = op.split('(')[1].split(')')[0].split(',')
                for u in list(G.nodes()):
                    v = int(u)
                    for switch in switches:
                        v ^= 1 << int(switch)
                    G.add_edge(u, v)
            path = nx.shortest_path(G, source=0, target=goal)
            print(f"Line {linecount} has shortest path of length {len(path) - 1}")
            ops_count += len(path) - 1
            linecount += 1
    print(f"Total ops count {ops_count}")


def factory_buttons_joltage(filepath):
    print(check_available_solvers())
    solver = pyo.SolverFactory("appsi_highs")
    with open(filepath, 'r') as file:
        lines = file.readlines()
        linecount = 0
        ops_count = 0
        for line in lines:
            final_joltages = line.split('{')[1].split('}')[0].split(',')
            n_buttons = len(final_joltages)
            ops = line.split(']')[1].split('{')[0].strip().split(' ')
            ops_by_button = {idx: [] for idx in range(n_buttons)}
            for idx in range(len(ops)):
                switches = ops[idx].split('(')[1].split(')')[0].split(',')
                for switch in switches:
                    ops_by_button[int(switch)].append(idx)

            model = pyo.ConcreteModel()
            model.presses = pyo.Var(range(len(ops)), domain=pyo.NonNegativeIntegers)
            model.obj = pyo.Objective(expr=sum(model.presses[i] for i in range(len(ops))))
            model.cons = pyo.ConstraintList()
            for button in range(n_buttons):
                model.cons.add(expr=sum(model.presses[i] for i in ops_by_button[button]) == int(final_joltages[button]))
            solver.solve(model)

            objval = pyo.value(model.obj)
            print(f"Line {linecount} requires {objval} presses")
            ops_count += objval
            linecount += 1
    print(f"Total presses count {ops_count}")

if __name__ == '__main__':
    factory_buttons_switches("input.txt")
    factory_buttons_joltage("input.txt")
