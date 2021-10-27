import math
from itertools import combinations

# import matplotlib.pyplot as plt
# import networkx as nx


def get_distance(loc1: dict, loc2: dict) -> float:
    return round(math.sqrt((loc1["x"] - loc2["x"]) ** 2 + (loc1["y"] - loc2["y"]) ** 2), 1)


def get_nodes_paths(data: list) -> list:
    _dict = [{"path": f"{i[0]['id']}-{i[1]['id']}", "dist": get_distance(i[0], i[1])} for i in combinations(data, 2)]
    _dict["visit_time"] = None
    return _dict


def drop_field(d):
    return {k: d[k] for k in d.keys() - ["first_name", "last_name", "email", "phone_number"]}


def main_logic(data: dict) -> None:
    array = []
    for person in data["users"]:
        new_person = drop_field(person)
        print(new_person)
        array.append(new_person)
    # print(get_distance(array[0], array[1]))


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
