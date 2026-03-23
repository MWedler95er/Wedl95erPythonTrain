"""Graph struktur"""


class GraphNode:
    def __init__(self, value):
        self.value = value
        self.nachbarn = []


berlin = GraphNode("Berlin")
muenchen = GraphNode("München")
hamburg = GraphNode("Hamburg")
berlin.nachbarn.append(muenchen)
berlin.nachbarn.append(hamburg)
muenchen.nachbarn.append(berlin)
muenchen.nachbarn.append(hamburg)
hamburg.nachbarn.append(berlin)


for city in [berlin, muenchen, hamburg]:
    neighbor_names = [neighbor.value for neighbor in city.nachbarn]
    print(f"{city.value} hat Nachbarn: {', '.join(neighbor_names)}")
