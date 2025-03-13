class Area:
    def __init__(self, name):
        self.name = name
        self.subareas = []
        
    # TODO: Define the add_subarea method to add a subarea to a given area
    def add_subarea(self, sub_area_name):
        self.subareas.append(Area(sub_area_name))
         
    # TODO: Define the dfs_traversal method to perform a depth-first search traversal over the areas
    def dfs_traversal(self, visited=None):
        if visited is None:
            visited = set()
        
        print(self.name + '->', end=' ')
        visited.add(self.name)
        
        for sub_area in self.subareas:
            sub_area.dfs_traversal(visited)


# TODO: Construct a tree to represent areas of a city
Cdmx = Area('Mexico City')
Cdmx.add_subarea('Historic Center')
Cdmx.add_subarea('Coyoacan')
Cdmx.add_subarea('Ciudad Satelite')

historic_center_area = Cdmx.subareas[0]
historic_center_area.add_subarea('Zocalo')
historic_center_area.add_subarea('Tepito')

coyoacan_area = Cdmx.subareas[1]
coyoacan_area.add_subarea('Coyoacan Center')

coyoacan_center_sub_area = coyoacan_area.subareas[0]
coyoacan_center_sub_area.add_subarea('Barrio Santa Catarina')

ciudad_satelite = Cdmx.subareas[2]

# TODO: Conduct a DFS traversal to print all areas
Cdmx.dfs_traversal()
