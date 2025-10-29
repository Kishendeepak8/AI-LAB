# ==============================
# Alpha-Beta Pruning with Tree Visualization
# ==============================

import math
import networkx as nx
import matplotlib.pyplot as plt

# ------------------------------
# 1️⃣ Define the Game Tree
# ------------------------------
tree = {
    'root': [['A1', 'A2']],   # MAX node
    'A1': [['B1', 'B2']],     # MIN node
    'A2': [['B3', 'B4']],     # MIN node
    'B1': [10, 9],            # MAX nodes
    'B2': [14, 18],
    'B3': [5, 4],
    'B4': [50, 3]
}

# ------------------------------
# 2️⃣ Alpha-Beta Pruning Algorithm
# ------------------------------
visited_edges = []     # Keep track of explored edges
pruned_edges = []      # Keep track of pruned edges

def minimax(node, depth, alpha, beta, isMax):
    # If node is terminal (contains numeric values)
    if isinstance(tree[node][0], int):
        return max(tree[node]) if isMax else min(tree[node])

    if isMax:
        value = -math.inf
        for child in tree[node][0]:
            visited_edges.append((node, child))
            eval_val = minimax(child, depth + 1, alpha, beta, False)
            value = max(value, eval_val)
            alpha = max(alpha, eval_val)
            if beta <= alpha:
                # Prune remaining children
                remaining = tree[node][0][tree[node][0].index(child)+1:]
                for c in remaining:
                    pruned_edges.append((node, c))
                break
        return value
    else:
        value = math.inf
        for child in tree[node][0]:
            visited_edges.append((node, child))
            eval_val = minimax(child, depth + 1, alpha, beta, True)
            value = min(value, eval_val)
            beta = min(beta, eval_val)
            if beta <= alpha:
                # Prune remaining children
                remaining = tree[node][0][tree[node][0].index(child)+1:]
                for c in remaining:
                    pruned_edges.append((node, c))
                break
        return value

# ------------------------------
# 3️⃣ Run Alpha-Beta from Root
# ------------------------------
root_value = minimax('root', 0, -math.inf, math.inf, True)
print("Final Value at Root Node:", root_value)

# ------------------------------
# 4️⃣ Build a Graph for Visualization
# ------------------------------
G = nx.DiGraph()

# Add all nodes and edges
for parent, children in tree.items():
    if isinstance(children[0], int):  # leaf node
        continue
    for child in children[0]:
        G.add_edge(parent, child)

# Add leaf nodes and their values
for node, children in tree.items():
    if isinstance(children[0], int):
        for i, val in enumerate(children):
            leaf_name = f"{node}_{val}"
            G.add_edge(node, leaf_name)
            G.nodes[leaf_name]["label"] = str(val)

# ------------------------------
# 5️⃣ Draw the Graph
# ------------------------------
pos = nx.spring_layout(G, seed=42)  # layout
plt.figure(figsize=(10, 7))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", arrows=True)

# Highlight visited (explored) edges
nx.draw_networkx_edges(G, pos, edgelist=visited_edges, width=3, edge_color="green", label="Explored")

# Highlight pruned (cutoff) edges
nx.draw_networkx_edges(G, pos, edgelist=pruned_edges, width=3, edge_color="red", style="dashed", label="Pruned")

# Label leaf nodes with their numeric values
labels = {n: G.nodes[n].get("label", n) for n in G.nodes()}
nx.draw_networkx_labels(G, pos, labels, font_size=10)

plt.title(f"Alpha-Beta Pruning Tree (Root Value = {root_value})")
plt.legend()
plt.show()
