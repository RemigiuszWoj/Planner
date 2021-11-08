import math
from itertools import combinations, permutations

# import matplotlib.pyplot as plt
# import networkx as nx
START_X = 0
START_Y = 0


def get_distance(loc1: dict, loc2: dict) -> float:
    return round(math.sqrt((loc1["x"] - loc2["x"]) ** 2 + (loc1["y"] - loc2["y"]) ** 2), 1)


def get_nodes_paths(data: list) -> list:
    _dict = [{"path": f"{i[0]['id']}-{i[1]['id']}", "dist": get_distance(i[0], i[1])} for i in combinations(data, 2)]
    return _dict


def drop_field(d: dict) -> dict:
    return {k: d[k] for k in d.keys() - ["first_name", "last_name", "email", "phone_number"]}


def insert_start(idx: int, _list: list):
    _list.insert(idx, {"id": 0, "x": START_X, "y": START_Y, "visit_time": 0})


def total_single_time(way: list, nodes: list) -> float:
    total_time = 0

    for i in range(len(way)):
        if i == 0:
            var = [node for node in nodes if way[0] == node["id"]]
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


def main_logic(data: dict) -> None:

    # list representing users as nodes with pos_x, pos_y, id
    nodes = [drop_field(p) for p in data["users"]]
    tab = []
    for i in permutations([node["id"] for node in nodes]):
        # tab.append((i, total_single_time(list(i), nodes)))
        tab.append(more_docs(list(i), nodes))
    # for i in tab:
    #     print(i)
    # print(min(tab, key=lambda x: x[0][1]))
    # print(len(tab), flush=True)
    n_tab = []
    for i in tab:
        n_tab.append(min(i, key=lambda x: x[1]))
    print(min(n_tab, key=lambda x: x[1]))

    # print(i, flush=True)
    #
    # tutaj bedzie podzial listy na podlisty
    #

    # aktualizacja poczatku i konca kazdej z list o pozycje startowa
    # insert_start(0, nodes)

    #
    # wyliczenie dlugosci sciezek pomiedzy wierzcholkami
    #

    #
    # miliony iteracji
    #

    return nodes


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
