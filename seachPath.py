# 18142222, Ritthikiet Methaviriyavanich
# AI - Lab 1

from collections import deque
import heapq

roadmap_with_distances = {  'arad': {'sibiu': 140, 'timisoara': 118, 'zerind': 75},
                            'bucharest': {'fagaras': 211, 'giurgiu': 90, 'pitesti': 101, 'urziceni': 85},
                            'craiova': {'dobreta': 120, 'pitesti': 138, 'rimnicu vilcea': 146},
                            'dobreta': {'craiova': 120, 'mehadia': 75},
                            'eforie': {'hirsova': 86},
                            'fagaras': {'bucharest': 211, 'sibiu': 99},
                            'giurgiu': {'bucharest': 90},
                            'hirsova': {'eforie': 86, 'urziceni': 98},
                            'iasi': {'neamt': 87, 'vaslui': 92},
                            'lugoj': {'mehadia': 70, 'timisoara': 111},
                            'mehadia': {'dobreta': 75, 'lugoj': 70},
                            'neamt': {'iasi': 87},
                            'oradea': {'sibiu': 151, 'zerind': 71},
                            'pitesti': {'bucharest': 101, 'craiova': 138, 'rimnicu vilcea': 97},
                            'rimnicu vilcea': {'craiova': 146, 'pitesti': 97, 'sibiu': 80},
                            'sibiu': {'arad': 140, 'fagaras': 99, 'oradea': 151, 'rimnicu vilcea': 80},
                            'timisoara': {'arad': 118, 'lugoj': 111},
                            'urziceni': {'bucharest': 85, 'hirsova': 98, 'vaslui': 142},
                            'vaslui': {'iasi': 92, 'urziceni': 142},
                            'zerind': {'arad': 75, 'oradea': 71}}


def BFS_simple(graph, start, goal):

    queue = deque([(start, [], 0)])  # [city, path, distance]
    explored = set()

    if start not in graph or goal not in graph:
        return None, 0
    
    while queue:
        current_city, path, total_distance = queue.popleft()
        explored.add(current_city)

        if current_city == goal:
            return path + [current_city], total_distance
        
        for adj_city, distance in graph[current_city].items():
            if adj_city not in explored:
                queue.append((adj_city, path + [current_city], total_distance + distance))

    return None, 0


def shortest_best_path(graph, start, goal): # dijkstra

    heap = [(0, start, [])]  # [total_distance, city, path]
    explored = set()

    if start not in graph or goal not in graph:
        return None, 0

    while heap:
        total_distance, current_city, path = heapq.heappop(heap)
        explored.add(current_city)
        
        if current_city == goal:
            return path + [current_city], total_distance
        
        for adj_city, distance in graph[current_city].items():
            if adj_city not in explored:
                heapq.heappush(heap, (total_distance + distance, adj_city, path + [current_city]))
            
    return None, 0


def printPath(path, start_city, goal_city, total_distance):
    
    if path:
        print(f"\nShortest path from {start_city} to {goal_city}:")
        print(' -> '.join(path))
        print(f"Total distance: {total_distance} km")
    else:
        print(f"No path found, {start_city} or {goal_city} city is not on the map.")


def main():

    start_city = input("Enter the start city: ").lower()
    goal_city = input("Enter the goal city: ").lower()

    mode = int(input("""Choices:
            1. BFS (generic)
            2. Shortest path (dijkstra)
    Select number: """))

    if mode == 1:
        shortest_path, total_distance = BFS_simple(roadmap_with_distances, start_city, goal_city)
    elif mode == 2:
        shortest_path, total_distance = shortest_best_path(roadmap_with_distances, start_city, goal_city)

    printPath(shortest_path, start_city, goal_city, total_distance)


if __name__ == "__main__":
    main()