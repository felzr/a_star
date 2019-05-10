import math
import dists
#Codigo de Felipe Ramos e Luiz Rodrigo Mottin

class Node():
    def __init__(self, name, current_dist, dist_from_prev, dist_to_goal, path = []):
        self.name = name
        self.current_dist = current_dist
        self.dist_from_prev = dist_from_prev
        self.dist_to_goal = dist_to_goal
        self.total_dist = self.current_dist + self.dist_from_prev
        self.cost = self.current_dist + self.dist_from_prev + self.dist_to_goal
        self.path = path[:]
        self.path.append(name)
    
    def __str__(self):
        return "<a:%s cost: b:%s>" % (self.name, self.cost)
    
    def __repr__(self):
        return "<a:%s cost: b:%s>" % (self.name, self.cost)

def a_star(start, goal):
    """
    Retorna uma lista com o caminho de start até 
    goal segundo o algoritmo A*
    """

    list_to_process = []
    arrived = False
    next_node = Node(start, 0, 0, 0)
    while not arrived:
        next_city_nodes = dists.dists[next_node.name]

        for name, distance in next_city_nodes:
            dist_to_goal = dists.straight_line_dists_from_bucharest[name]
            list_to_process.append(
                Node(name, next_node.total_dist, distance, dist_to_goal, next_node.path))

        list_to_process.sort(key=lambda node: node.cost)

        next_node = list_to_process.pop(0)
        print(f"-->>Testando o caminho")
        print(next_node.path)
        if next_node.name == goal:
            arrived = True

    return next_node.path

path = a_star('Pitesti', 'Bucharest')
print('-' * 50)
print('Caminho escolhido:')
print(path)
