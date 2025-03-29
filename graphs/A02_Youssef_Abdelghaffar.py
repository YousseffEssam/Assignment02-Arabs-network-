import networkx as nx  # type: ignore
import matplotlib.pyplot as plt  # type: ignore

# Create a Graph
G = nx.Graph()

# Arab countries with approximate land area (in thousand km²) for scaling node sizes
country_data = {
    "Algeria": (4000, "green"), "Bahrain": (300, "red"), "Djibouti": (600, "blue"),
    "Egypt": (2500, "yellow"), "Iraq": (1000, "black"), "Jordan": (400, "green"), "Kuwait": (350, "red"),
    "Lebanon": (350, "white"), "Libya": (2000, "green"), "Mauritania": (1800, "orange"), "Morocco": (1800, "red"),
    "Oman": (500, "red"), "Palestine": (2000, "pink"), "Qatar": (300, "maroon"), "Saudi Arabia": (2600, "green"),
    "Somalia": (900, "blue"), "Sudan": (1860, "red"), "Syria": (300, "red"), "Tunisia": (300, "red"),
    "UAE": (400, "red"), "Yemen": (800, "red")
}

# Edges representing neighboring relationships
edges = [
    ("Algeria", "Tunisia"), ("Algeria", "Libya"), ("Algeria", "Morocco"),
    ("Bahrain", "Saudi Arabia"), 
    ("Djibouti", "Somalia"), ("Djibouti", "Yemen"),
    ("Egypt", "Libya"), ("Egypt", "Sudan"), ("Egypt", "Palestine"),
    ("Iraq", "Syria"), ("Iraq", "Jordan"), ("Iraq", "Saudi Arabia"), ("Iraq", "Kuwait"),
    ("Jordan", "Saudi Arabia"), ("Jordan", "Syria"), ("Jordan", "Palestine"),
    ("Kuwait", "Saudi Arabia"),
    ("Lebanon", "Syria"), 
    ("Libya", "Tunisia"), ("Libya", "Sudan"),
    ("Mauritania", "Morocco"), ("Mauritania", "Algeria"),
    ("Morocco", "Algeria"),
    ("Oman", "UAE"), ("Oman", "Saudi Arabia"), ("Oman", "Yemen"), 
    ("Qatar", "Saudi Arabia"),
    ("Saudi Arabia", "UAE"), ("Saudi Arabia", "Yemen"),
    ("Somalia", "Djibouti"),
    ("Syria", "Lebanon"),
    ("Tunisia", "Algeria"),
    ("UAE", "Saudi Arabia"),
    ("Yemen", "Saudi Arabia")
]

# Create graph
G = nx.Graph()
G.add_nodes_from(country_data.keys())
G.add_edges_from(edges)

# Extract node colors and sizes
node_colors = [country_data[country][1] for country in G.nodes()]
node_sizes = [country_data[country][0] / 3 for country in G.nodes()]  # Scaling for visibility

# Set figure and background color
plt.figure(figsize=(16,12), facecolor="grey")
ax = plt.gca()
ax.set_facecolor("grey")  # Set axes background to black

# Generate layout
pos = nx.spring_layout(G, seed=42)

# Draw graph with black background settings
nx.draw(
    G, pos, with_labels=True, 
    node_color=node_colors, node_size=node_sizes, 
    font_size=10, font_color="white", edge_color="white", width=3
)

# Set bold white title
plt.title("Arab Countries Network", fontsize=40, color="cyan", fontweight="bold")

# Save the graph with black background
path = r"C:\Users\Nehad\Desktop\Youssef Python session02\images\A02_Youssef_Abdelghaffar.jpg"
plt.savefig(path, format="PNG", facecolor="grey")  # Ensure black background in saved image

# Show the plot
#plt.show()
