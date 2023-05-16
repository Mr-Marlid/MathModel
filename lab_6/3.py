import networkx as nx
import matplotlib.pyplot as plt

# Создание графа
G = nx.DiGraph()

# Добавление вершин в граф
G.add_nodes_from(["G(Exp(2,0,15))", "Q(Sif_1)", "R(M_ts)", "Decision", "Noh_1", "Q(Sif_2)", "Noh_2", "G(20.5)", "T"])

# Добавление ребер (соединений) между вершинами
G.add_edges_from([("G(Exp(2,0,15))", "Q(Sif_1)"),
                  ("Q(Sif_1)", "R(M_ts)"),
                  ("R(M_ts)", "Decision"),
                  ("Decision", "Noh_1"),
                  ("Decision", "Noh_2"),
                  ("Noh_1", "Q(Sif_2)"),
                  ("Q(Sif_2)", "R(M_ts)"),
                  ("R(M_ts)", "T"),
                  ("G(20.5)", "Q(Sif_2)")])

# Визуализация графа
pos = nx.spring_layout(G, seed=70)
nx.draw_networkx_edges(G, pos, node_size=1500)

# Рисование разных форм узлов с помощью matplotlib
for node, (x, y) in pos.items():
    if "G" in node or "T" in node:
        plt.scatter(x, y, c='lightblue', marker='o', s=1500)
    elif "Q" in node:
        plt.scatter(x, y, c='lightblue', marker='s', s=1500)
    elif "R" in node:
        plt.scatter(x, y, c='lightblue', marker='d', s=1500)
    elif "Decision" in node:
        plt.scatter(x, y, c='lightblue', marker='^', s=1500)
    elif "Noh" in node:
        plt.scatter(x, y, c='lightblue', marker='>', s=1500)
    plt.text(x, y, node, ha='center', va='center', fontsize=7, fontweight='bold')

plt.axis('off')
plt.show()
