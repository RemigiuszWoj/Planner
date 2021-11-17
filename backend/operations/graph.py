import math
import random
from copy import deepcopy
from itertools import permutations

START_X = 0
START_Y = 0


def get_distance(loc1: dict, loc2: dict) -> float:
    return round(math.sqrt((loc1["x"] - loc2["x"]) ** 2 + (loc1["y"] - loc2["y"]) ** 2), 1)


def drop_field(d: dict) -> dict:
    return {k: d[k] for k in d.keys() - ["first_name", "last_name", "email", "phone_number"]}


def total_single_time(way: list, nodes: list) -> float:
    total_time = 0

    for i in range(len(way)):
        if i == 0:
            var = [node for node in nodes if way[0] == node["id"]]  # client 1

            total_time += (
                get_distance({"id": 0, "x": START_X, "y": START_Y, "visit_time": 0}, var[0]) + var[0]["visit_time"]
            )
        else:
            var1 = [node for node in nodes if way[i] == node["id"]]
            var2 = [node for node in nodes if way[i - 1] == node["id"]]
            total_time += get_distance(var1[0], var2[0]) + var1[0]["visit_time"]
    return round(total_time, 2)


def more_docs(doc1: list, nodes: list) -> list:
    doc2 = []
    total_time = []

    while True:
        t1 = total_single_time(doc1, nodes)
        t2 = total_single_time(doc2, nodes)
        greater = t1 if t1 >= t2 else t2
        total_time.append((f"{doc1}-{doc2}", round(greater, 2)))
        try:
            doc2.append(doc1.pop())
        except IndexError:
            break
    return total_time


def main_logic(data: dict) -> tuple:
    nodes = [drop_field(p) for p in data["users"]]

    if len(nodes) <= 8:
        tab = [more_docs(list(i), nodes) for i in permutations([node["id"] for node in nodes])]
        n_tab = [min(i, key=lambda x: x[1]) for i in tab]
        return min(n_tab, key=lambda x: x[1])

    else:
        nodes = [drop_field(p) for p in data["users"]]
        total_time = []

        for _ in range(100_000):
            doc1 = []
            doc2 = []
            nodes_copy = [node["id"] for node in nodes]

            while nodes_copy:
                if random.randint(1, 1000) % 2 == 0:
                    doc1.append(nodes_copy.pop(random.randint(0, len(nodes_copy) - 1)))
                else:
                    doc2.append(nodes_copy.pop(random.randint(0, len(nodes_copy) - 1)))

            t1 = total_single_time(doc1, nodes)
            t2 = total_single_time(doc2, nodes)
            greater = t1 if t1 >= t2 else t2
            total_time.append((f"{doc1}-{doc2}", greater))

        return min(total_time, key=lambda x: x[1])


def test(trasa):
    trasa.pop()
    trasa.pop(0)

    doc1 = trasa[: trasa.index(0)]
    doc2 = trasa[trasa.index(0) + 1 :]

    t1 = total_single_time(doc1, trasa)
    t2 = total_single_time(doc2, trasa)
    greater = t1 if t1 >= t2 else t2
    return greater


# def main_logic(data: dict) -> tuple:
#     nodes = [drop_field(p) for p in data["users"]]

#     if len(nodes) <= 8:
#         tab = [more_docs(list(i), nodes) for i in permutations([node["id"] for node in nodes])]
#         n_tab = [min(i, key=lambda x: x[1]) for i in tab]
#         return min(n_tab, key=lambda x: x[1])

#     else:
#         nodes = [drop_field(p) for p in data["users"]]
#         total_time = []
#         T0, Tk, lam = 1000, 0.1, 0.995
#         T = T0
#         nodes_copy = [node["id"] for node in nodes]
#         t0 = deepcopy(nodes_copy)
#         t0.insert(0, 0)
#         t0.insert(5, 0)
#         t0.append(0)
#         t = deepcopy(t0)
#         tb = deepcopy(t0)
#         cmax_best = test(tb)
#         while T > Tk:

#             tprime = deepcopy(t)
#             cmax = test(t)
#             tp1 = random.randint(1, len(nodes) - 1)
#             tp2 = random.randint(1, len(nodes) - 1)
#             tprime[tp1], tprime[tp2] = tprime[tp2], tprime[tp1]
#             cmaxprime = test(tprime)

#             if cmaxprime < cmax_best:
#                 cmax_best = cmaxprime
#                 tb = deepcopy(tprime)
#             if cmaxprime <= cmax:
#                 t = tprime
#             else:
#                 delta = cmaxprime - cmax
#                 p = math.exp(-delta / T)
#                 random1 = random.randint(0, 100) / 100
#                 if p < random1:
#                     t = tprime

#             # t1 = total_single_time(doc1, nodes)
#             # t2 = total_single_time(doc2, nodes)
#             # greater = t1 if t1 >= t2 else t2
#             # total_time.append((f"{doc1}-{doc2}", greater))

#             T = lam * T

#         print(cmax)
#         print(cmaxprime)
#         return min(total_time, key=lambda x: x[1])
