
import pandas as pd
from rdflib import Graph, URIRef, Literal, RDF
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv("legacy_internship_records_final.csv")

print("csv loaded")

Initial_T_Box = {
        "class": "Intern",
        "datatype_properties": [
                "intern_id",
                "name",
                "guild",
                "xp_earned",
                "completed_tasks",
                "join_date",
                "performance_rating"
        ],
        "object_properties":[]
}

Final_T_Box = {
        "class": "Intern",
        "datatype_properties": [
                "hasInternID",
                "hasName",
                "hasGuild",
                "earnedXP",
                "completedTasks",
                "joinedOn",
                "hasPerformanceRating"
        ],
        "object_properties":[]
        
}

print("t_box created")
property_mapping = {
    "intern_id": "hasInternID",
    "name": "hasName",
    "guild": "hasGuild",
    "xp_earned": "earnedXP",
    "completed_tasks": "completedTasks",
    "join_date": "joinedOn",
    "performance_rating": "hasPerformanceRating"
}

graph = Graph()

print("number of triples:", len(graph))

intern_class = URIRef("http://example.org/Intern")

for i in range(len(df)):
    row = df.iloc[i]
    intern = URIRef(f"http://example.org/intern/{row['intern_id']}")
    graph.add((intern, RDF.type, intern_class))
    for csv_column, rdf_property in property_mapping.items():
        property_uri = URIRef(f"http://example.org/{rdf_property}")
        value = Literal(row[csv_column])
        graph.add((intern, property_uri, value))

print("number of triples:", len(graph))

print("graph created")

graph.serialize(destination="knowledge_graph.ttl", format="turtle")
print("graph turtle file created")


G = nx.DiGraph()
G.add_node("INT-001")
G.add_node("Aidan Vance")
G.add_node("Archivist")
G.add_node("120")
G.add_node("4")
G.add_node("2025-01-15")
G.add_node("Excellent")
G.add_edge("INT-001", "Aidan Vance", label="hasName")
G.add_edge("INT-001", "Archivist", label="hasGuild")
G.add_edge("INT-001", "120", label="earnedXP")
G.add_edge("INT-001", "4", label="completedTasks")
G.add_edge("INT-001", "2025-01-15", label="joinedOn")
G.add_edge("INT-001", "Excellent", label="hasPerformanceRating")

pos = nx.spring_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2500,
    font_size=8
)

edge_labels = nx.get_edge_attributes(G, "label")

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_size=7
)

plt.savefig("proof.png")
plt.show()


with open("kg_report.txt", "w", encoding="utf-8") as file:
    file.write("KNOWLEDGE GRAPH REPORT\n")
    file.write("Class: " + Final_T_Box["class"] + "\n")
    file.write("Datatype Properties: " + str(len(Final_T_Box["datatype_properties"])) + "\n")
    file.write("Number of Individuals: " + str(len(df)) + "\n")
    file.write("Number of RDF Triples: " + str(len(graph)) + "\n")
    file.write("FILES GENERATED\n")
    file.write("knowledge_graph.ttl\n")
    file.write("proof.png\n")
    file.write("kg_report.txt\n\n")
print("kg_report.txt generated successfully")