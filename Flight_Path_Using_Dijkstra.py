import networkx as nx
import matplotlib.pyplot as plt

# Build a weighted undirected graph
G = nx.Graph()

# Defining weight of edges
edges = [
    ('San Francisco', 'Denver', 1000),
    ('San Francisco', 'Chicago', 1500),
    ('Los Angeles', 'Denver', 1400),
    ('Los Angeles', 'Dallas', 1100),
    ('Denver', 'Dallas', 600),
    ('Denver', 'Chicago', 500),
    ('Dallas', 'Chicago', 800),
    ('Chicago', 'New York', 700),
    ('Chicago', 'Boston', 900),
    ('New York', 'Boston', 300)
]

G.add_weighted_edges_from(edges)

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1200, font_weight='bold')
edge_labels = {(u, v): f"{d}" for u, v, d in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Original Flight Graph")
plt.axis('off')
plt.show()

# From to location
source = "Los Angeles"
target = "New York"
shortest_path = nx.dijkstra_path(G, source, target)
shortest_path_length = nx.dijkstra_path_length(G, source, target)
shortest_edges = list(zip(shortest_path[:-1], shortest_path[1:]))

plt.figure(figsize=(10, 6))

# Draw all nodes
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=1200)
nx.draw_networkx_labels(G, pos, font_weight='bold')

# Highlight shortest path nodes
nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_color='lightcoral', node_size=1300)

# Draw all edges
nx.draw_networkx_edges(G, pos, alpha=0.3)

# Highlight shortest path edges
nx.draw_networkx_edges(G, pos, edgelist=shortest_edges, edge_color='red', width=3)

path_edge_labels = {(u, v): f"{G[u][v]['weight']}" for u, v in shortest_edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=path_edge_labels)

plt.title(f"Shortest Path from {source} to {target} (Distance: {shortest_path_length} miles)")
plt.axis('off')
plt.show()