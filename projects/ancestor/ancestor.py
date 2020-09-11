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

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

def earliest_ancestor(ancestors, starting_node):
    #DAG - directed acyclic graph, you can never get back to where you start and all the edges move one direction 

    ancestors_graph = Graph() #make a graph
    for pair in ancestors: #the input "ancestors" is fed in as a long list of pairs - each pair has an index 0, 1
        ancestors_graph.add_vertex(pair[0]) #add pair at index 0 as a vertex
        ancestors_graph.add_vertex(pair[1]) #add pair at index 1 as a vertex
        ancestors_graph.add_edge(pair[1], pair[0]) #create an edge that travels "backwards" from index 1 to index 0 - we need to move up! 
    
    queue = Queue() #get your queue ready
    queue.enqueue([starting_node]) #queue up a path with just the starting node 
    max_path_length = 1 #longest path we've found so far
    earliest_ancestor = -1 #this will become the id of the furthest away vertex we find - if we dont find any futher away verticies it stays -1 and returns -1 as per instructions 
    while queue.size() > 0: #while there is stuff in the queue (aka a path with vertices)
        path = queue.dequeue() #take the head of the queue (the path)
        current_vertex = path[-1] #take the last value of the path(first time around its just the starting vertex, second time it will be a neighbour)
        if (len(path) > max_path_length) or (len(path) >= max_path_length and current_vertex < earliest_ancestor): 
            #if the length of the path is longer than the longest path we've ever found OR 
            # is equal to the longest path we've found(or greater than), but the id number of the current vertex is smaller than our current earliest ancestor (as per instructions), 
            earliest_ancestor = current_vertex #assign earliest ancestor to the end of the path we are on 
            max_path_length = len(path) #assign to length of current path 
        for edge in ancestors_graph.vertices[current_vertex]: #look at the edges aka neighbours of the current vertex
            path_copy = list(path) #make a copy of the path(includes what you've already looked at)
            path_copy.append(edge) #add the neighbours
            queue.enqueue(path_copy) #queue up the new path to start looking again 

            #ultimately, the algorithim with reach a point where it can't find a longer path, and there are no more edges(neighbours). It will return the end of that path as the earliest ancestor. 
    
    return earliest_ancestor



    
    

    






   