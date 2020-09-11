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
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        #Find vertex v1 and add v2 to the set of edges 
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None 

    def bft(self, starting_vertex): #here we are just doiung something at every ndoe
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #Create an empty queue and enqueue the starting_vertex
        #while queue is not empty
            #get the current vertex (dequeue from queye)
            #print the current vertex
            #qeue up all the current vertex's neighbours (so we can vist them next)
        
        queue = Queue()
        visted = set()
        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            current_vertex = queue.dequeue()
            if current_vertex not in visted:
                print(current_vertex)
                visted.add(current_vertex)
                if self.vertices[current_vertex]:
                    for edge in self.vertices[current_vertex]:
                        queue.enqueue(edge)
        
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visted = set()
        stack.push(starting_vertex)
        while stack.size() > 0:
            current_vertex = stack.pop()
            if current_vertex not in visted:
                print(current_vertex)
                visted.add(current_vertex)
                if self.vertices[current_vertex]:
                    for edge in self.vertices[current_vertex]:
                        stack.push(edge)

    def dft_recursive(self, starting_vertex, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(starting_vertex)
        print(starting_vertex)
        for edge in self.vertices[starting_vertex]:
            if edge not in visited:
                self.dft_recursive(edge,visited)

        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
    

    def bfs(self, starting_vertex, destination_vertex): 
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #Create an empty queue and enqueue the starting_vertex
        #create an empty set to track visited vertices 
        #while queue is not empty
            #get the current vertex (dequeue from queue)
            #check if the current vertex is the destination 
            #if it is, stop and return 
            #else add to visited 
            #qeue up all the current vertex's neighbours (so we can vist them next)
        queue = Queue()
        visted = set()
        queue.enqueue([starting_vertex])
        while queue.size() > 0:
            path = queue.dequeue()
            current_vertex = path[-1]
            if current_vertex not in visted:
                if current_vertex == destination_vertex:
                    return path 
                visted.add(current_vertex)
                if self.vertices[current_vertex]:
                    for edge in self.vertices[current_vertex]:
                        new_path = list(path)
                        new_path.append(edge)
                        queue.enqueue(new_path)         

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visted = set()
        stack.push([starting_vertex])
        while stack.size() > 0:
            path = stack.pop()
            current_vertex = path[-1]
            if current_vertex not in visted:
                if current_vertex == destination_vertex:
                    return path 
                visted.add(current_vertex)
                if self.vertices[current_vertex]:
                    for edge in self.vertices[current_vertex]:
                        new_path = list(path)
                        new_path.append(edge)
                        stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        
        if path is None:
            path = []
        
        visited.add(starting_vertex)
        new_path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return new_path
        for edge in self.vertices[starting_vertex]:
            if edge not in visited:
                edge_path = self.dfs_recursive(edge, destination_vertex, visited, new_path)
                if edge_path:
                    return edge_path

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
