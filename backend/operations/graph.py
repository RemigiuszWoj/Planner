import math
from itertools import combinations

import matplotlib.pyplot as plt
import networkx as nx


def get_distance(loc1: dict, loc2: dict) -> float:
    return math.sqrt((loc1["position_x"] - loc2["position_x"]) ** 2 + (loc1["position_y"] - loc2["position_y"]) ** 2)


def get_nodes_paths(data: list) -> list:
    return [
        {"path": f"{i[0]['id']}-{i[1]['id']}", "dist": round(get_distance(i[0], i[1]), 1)}
        for i in combinations(data, 2)
    ]


def graph(data: list) -> None:

    # create empty graph
    G = nx.Graph()

    # insert start point
    start = {
        "id": 0,
        "position_x": 0,
        "position_y": 0,
    }

    data.insert(0, start)

    # add nodes to graph from input data
    for ob in data:
        G.add_node(ob["id"], pos=(ob["position_x"], ob["position_y"]))

    # create edges between nodes, as a tuple of references to each node
    G.add_edges_from(combinations([i["id"] for i in data], 2))

    w = nx.johnson(G, weight="weight")
    print(w)
    nx.draw(G, nx.get_node_attributes(G, "pos"), with_labels=True)
    plt.show()

    # print("All distances: ", get_nodes_paths(data))


people = [
    {
        "id": 1,
        "first_name": "Jagoda",
        "last_name": "Grabik",
        "email": "jagoda.grabik.wp.pl",
        "phone_number": "433067257",
        "position_x": -2,
        "position_y": -2,
    },
    {
        "id": 2,
        "first_name": "Julia",
        "last_name": "Piotrowicz",
        "email": "julia.piotrowicz.onet.pl",
        "phone_number": "178416098",
        "position_x": -20,
        "position_y": -8,
    },
    {
        "id": 3,
        "first_name": "Hubert",
        "last_name": "Galazka",
        "email": "hubert.galazka.wp.pl",
        "phone_number": "107910397",
        "position_x": -14,
        "position_y": 13,
    },
    {
        "id": 4,
        "first_name": "Wieslaw",
        "last_name": "Michalczyk",
        "email": "wieslaw.michalczyk.onet.pl",
        "phone_number": "520680593",
        "position_x": -20,
        "position_y": -10,
    },
    {
        "id": 5,
        "first_name": "Anna",
        "last_name": "Wlos",
        "email": "anna.wlos.wp.pl",
        "phone_number": "477362383",
        "position_x": 9,
        "position_y": 2,
    },
    # },
    # {
    #     "id": 6,
    #     "first_name": "Mateusz",
    #     "last_name": "Wojcik",
    #     "email": "mateusz.wojcik.wp.pl",
    #     "phone_number": "761661329",
    #     "position_x": -6,
    #     "position_y": 0,
    # },
    # {
    #     "id": 7,
    #     "first_name": "Tomasz",
    #     "last_name": "Wojcik",
    #     "email": "tomasz.wojcik.wp.pl",
    #     "phone_number": "780751665",
    #     "position_x": 8,
    #     "position_y": 10,
    # },
    # {
    #     "id": 8,
    #     "first_name": "Kamil",
    #     "last_name": "Galazka",
    #     "email": "kamil.galazka.gmail.com",
    #     "phone_number": "291747091",
    #     "position_x": -12,
    #     "position_y": -2,
    # },
]

graph(people)
