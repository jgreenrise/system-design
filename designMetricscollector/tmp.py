import networkx as nx
import matplotlib.pyplot as plt

# Input data
numCourses = 6
prerequisites = [[4,5],[4,0],[0,1],[1,2],[2,3],[4,3]]

# Create a directed graph
G = nx.DiGraph()

# Add nodes for each course
for course in range(numCourses):
    G.add_node(course)

# Add directed edges based on prerequisites
for prereq in prerequisites:
    G.add_edge(prereq[1], prereq[0])

# Create a layout for the nodes
pos = nx.spring_layout(G)

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10)
plt.title("Course Prerequisites")
plt.show()
