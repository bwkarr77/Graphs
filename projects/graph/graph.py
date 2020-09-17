"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        bft_queue = Queue()
        bft_queue.enqueue(starting_vertex)
        visited = []

        while bft_queue.size() > 0:
            vertex = bft_queue.dequeue()

            if vertex not in visited:
                visited.append(vertex)

                for neighbor in self.get_neighbors(vertex):
                    bft_queue.enqueue(neighbor)

        for each in visited:
            print(each)
        return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        dft_stack = Stack()
        dft_stack.push(starting_vertex)
        visited = []

        while dft_stack.size() > 0:
            vertex = dft_stack.pop()

            if vertex not in visited:
                visited.append(vertex)

                for neighbor in self.get_neighbors(vertex):
                    dft_stack.push(neighbor)

        for each in visited:
            print(each)
        return visited

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = []

        visited.append(starting_vertex)
        print(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

        # print('recursive:', visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        bfs_queue = Queue()
        # the Queue will be a list of the path we take, starting with starting_vertex
        bfs_queue.enqueue([starting_vertex])
        visited = set()

        while bfs_queue.size() > 0:
            cur_path = bfs_queue.dequeue()
            vertex = cur_path[-1]  # returns the LAST value in list (negative numbers go R to L)

            if vertex not in visited:
                if vertex == destination_vertex:
                    return cur_path

                visited.add(vertex)

                for neighbor in self.get_neighbors(vertex):
                    # new_path = cur_path  # not sure why this DOESN'T work?
                    new_path = list(cur_path)  # not sure why this DOES work?
                    new_path.append(neighbor)
                    bfs_queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        dft_stack = Stack()
        dft_stack.push([starting_vertex])
        visited = set()

        while dft_stack.size() > 0:
            cur_path = dft_stack.pop()
            vertex = cur_path[-1]  # negative numbers count from R to L, -1 is the last element

            if vertex not in visited:
                if vertex == destination_vertex:
                    return cur_path

                visited.add(vertex)

                for neighbor in self.get_neighbors(vertex):
                    # new_path = cur_path  # not sure why this DOESN'T work?
                    new_path = list(cur_path)  # not sure why this DOES work?
                    new_path.append(neighbor)
                    dft_stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if starting_vertex == destination_vertex:
            # return a list of path with the final value
            return [*path, starting_vertex]
            # [*path, starting_vertex]=> can also be = path.append(starting_vertex)
            # the [*path, val] turns: [[1,2,3], 4], into [1,2,3, 4]

        visited.add(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                # if neighbor isn't in visited, use recursion with neighbor as the starting point
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, [*path, starting_vertex])
                if new_path is not None:
                    return new_path

        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
