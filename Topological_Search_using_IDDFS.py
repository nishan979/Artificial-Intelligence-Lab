from collections import defaultdict

class TopologicalSortIDDFS:
    def __init__(self, total_vertices):
        self.graph = defaultdict(list)
        self.V = total_vertices
        self.topo_stack = []

    def add_edge(self, start, end):
        self.graph[start].append(end)

    def depth_limited_dfs(self, node, visited, current_depth, depth_limit):
        if current_depth > depth_limit:
            return
        visited[node] = True
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.depth_limited_dfs(neighbor, visited, current_depth + 1, depth_limit)
        if node not in self.topo_stack:
            self.topo_stack.append(node)

    def perform_topological_sort(self):
        for depth_limit in range(self.V):
            visited = [False] * self.V
            for vertex in range(self.V):
                if not visited[vertex]:
                    self.depth_limited_dfs(vertex, visited, 0, depth_limit)


        print("\nTopological Sort using IDDFS:")
        print(" → ".join(map(str, reversed(self.topo_stack))))

if __name__ == "__main__":
    print("Topological Sort Using IDDFS")
    
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))

    ts = TopologicalSortIDDFS(V)
    
    print("Enter the edges (format: u v):")
    for _ in range(E):
        u, v = map(int, input().split())
        ts.add_edge(u, v)
    
    ts.perform_topological_sort()
