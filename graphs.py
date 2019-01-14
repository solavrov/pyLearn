import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 1), (1, 4), (4, 2)])

node_colors = ['r', 'b', 'g', 'black', 'r']
edge_colors = ['b', 'r', 'b', 'r', 'r']

nx.draw(G,
        with_labels=True,
        node_color=node_colors,
        edge_color=edge_colors,
        node_shape='8',
        font_color='w',
        font_size=14,
        node_size=1000,
        width=2)

plt.show()


