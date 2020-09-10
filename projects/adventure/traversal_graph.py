class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)




class Traversal_Graph:

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

    def get_all_traversal_paths(self, starting_vertex):
        #Create a Quere
        queue = Queue()
        #create a visted list
        visited = {} #dictionary not a set 
        #add starting vertex to the Queue as a path
        queue.enqueue([starting_vertex])

        #WHile the Queue is not empty:
        while queue.size() > 0:
            #Deueue a current path
            current_path = queue.dequeue()
            #Get the current vertex from the end of the path
            current_vertex = current_path[-1]
            #If current vertex not in visted_set
            if current_vertex not in visited:
                visited[current_vertex] = current_path
                for edge in self.vertices[current_vertex]:
                    new_path = current_path.copy()
                    new_path.append(edge)
                    queue.enqueue(new_path)
                #add vertex to visited set
                #ALSO add the PATH that brought us to the vertex 
                #ie add a key and value to the visted Dictionary
                #key is the current vertex the value is the path 
                #queue up all neighbours as paths
        return visited 

