import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_node("a", pos=(1, 1), imie="anna", naz="ibisz", email="jebacdisa@wp.pl")
G.add_node("b", pos=(10, 2))

pos = nx.get_node_attributes(G, "pos")
imiona = nx.get_node_attributes(G, "imie")

print(G.nodes.data())
nx.draw(G, pos)
# save as png
plt.show()  # display
