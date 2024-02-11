import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('friendship_network.csv')

# Create the graph
g = nx.DiGraph()

# Add the edges to the graph
for i, row in df.iterrows():
    screen_name = row['screen_names']
    followers = set(row['followers'].split(','))
    friends = set(row['friends'].split(','))
    for follower in followers:
        g.add_edge(follower.strip(), screen_name)
    for friend in friends:
        g.add_edge(screen_name, friend.strip())

# Draw the graph using matplotlib
print('Number of Nodes :',g.number_of_nodes())
print('Number of Edges',g.number_of_edges())
nx.draw(g, with_labels=True, font_color="#A2A2A1FF", font_size=4, width=0.5, node_size=150, node_color='#333D79FF', arrowsize = 9)
plt.show()

## 3 Network Measures##
degree_sequence = [d for n, d in g.in_degree()]

# Plot the degree distribution as a histogram
plt.hist(degree_sequence, bins=30, color='#333D79FF')
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.title('Degree Distribution')
plt.show()

# Calculate the clustering coefficient
clustering = nx.clustering(g)
clustering_values = [c for n, c in clustering.items()]

# Plot the clustering coefficient as a histogram
plt.hist(clustering_values, bins=30, color='#333D79FF')
plt.xlabel('Clustering Coefficient')
plt.ylabel('Frequency')
plt.title('Clustering Coefficient Distribution')
plt.show()

# Calculate the PageRank
pagerank = nx.pagerank(g)
pagerank_values = [p for n, p in pagerank.items()]

# Plot the PageRank as a histogram
plt.hist(pagerank_values, bins=30, color='#333D79FF')
plt.xlabel('PageRank')
plt.ylabel('Frequency')
plt.title('PageRank Distribution')
plt.show()

closeness_centrality = nx.closeness_centrality(g)

# plot histogram of closeness centrality
plt.hist(list(closeness_centrality.values()), bins=20, color='#333D79FF')
plt.xlabel("Closeness")
plt.ylabel("Frequency")
plt.title("Closeness Centrality")
plt.show()

betweenness_centrality = nx.betweenness_centrality(g)

# plot histogram of betweenness_centrality
plt.hist(list(betweenness_centrality.values()), bins=20, color='#333D79FF')
plt.xlabel("Betweenness")
plt.ylabel("Frequency")
plt.title("Betweenness Centrality")
plt.show()