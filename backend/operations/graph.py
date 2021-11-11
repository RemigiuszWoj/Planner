import math
import random
from copy import deepcopy
from itertools import permutations

# import matplotlib.pyplot as plt
# import networkx as nx
START_X = 0
START_Y = 0


def get_distance(loc1: dict, loc2: dict) -> float:
    return round(math.sqrt((loc1["x"] - loc2["x"]) ** 2 + (loc1["y"] - loc2["y"]) ** 2), 1)


def drop_field(d: dict) -> dict:
    return {k: d[k] for k in d.keys() - ["first_name", "last_name", "email", "phone_number"]}


def insert_start(idx: int, _list: list):
    _list.insert(idx, {"id": 0, "x": START_X, "y": START_Y, "visit_time": 0})


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
    return total_time


def more_docs(doc1: list, nodes: list) -> list:
    doc2 = []
    total_time = []

    while True:
        t1 = total_single_time(doc1, nodes)
        t2 = total_single_time(doc2, nodes)
        greater = t1 if t1 >= t2 else t2
        total_time.append((f"{doc1}-{doc2}", greater))
        try:
            doc2.append(doc1.pop())
        except IndexError:
            break
    return total_time


def main_logic(data: dict) -> tuple:
    nodes = [drop_field(p) for p in data["users"]]
    # if len(nodes) <= 8:
    tab = [more_docs(list(i), nodes) for i in permutations([node["id"] for node in nodes])]
    n_tab = [min(i, key=lambda x: x[1]) for i in tab if i]
    return min(n_tab, key=lambda x: x[1])


# def main_logic(data):
#     print("*" * 20)
#     nodes = [drop_field(p) for p in data["users"]]
#     total_time = []

#     for i in range(100):
#         doc1 = []
#         doc2 = []
#         nodes_copy = [node["id"] for node in nodes]

#         while len(nodes_copy) != 0:
#             if random.randint(1, 100) % 2 == 0:
#                 doc1.append(nodes_copy.pop())
#             else:
#                 doc2.append(nodes_copy.pop())

#         t1 = total_single_time(doc1, nodes)
#         t2 = total_single_time(doc2, nodes)
#         greater = t1 if t1 >= t2 else t2
#         total_time.append((f"{doc1}-{doc2}", greater))
#     print(total_time)
#     n_tab = [min(i, key=lambda x: x[1]) for i in total_time if i]
#     return min(n_tab, key=lambda x: x[1])
# return ("[1]-[2,3]", 20)


# # create empty graph
# G = nx.Graph()

# # insert start point
# start = {
#     "id": 0,
#     "position_x": 0,
#     "position_y": 0,
# }

# data.insert(0, start)

# # add nodes to graph from input data
# for ob in data:
#     G.add_node(ob["id"], pos=(ob["position_x"], ob["position_y"]))

# # create edges between nodes, as a tuple of references to each node
# G.add_edges_from(combinations([i["id"] for i in data], 2))

# w = nx.johnson(G, weight="weight")
# print(w)
# nx.draw(G, nx.get_node_attributes(G, "pos"), with_labels=True)
# plt.show()

# # print("All distances: ", get_nodes_paths(data))
