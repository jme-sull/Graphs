from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

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

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

traversal_path = []
backtrack_path = []
##establish the direction of the backward traversal
backwards_traversal = {
    'n':'s',
    's':'n',
    'e':'w',
    'w':'e'
}

visited = {}
visited[player.current_room.id] =  player.current_room.get_exits()

while len(visited) < len(room_graph):
    current_room = player.current_room.id
    if current_room not in visited:
        visited[current_room] = player.current_room.get_exits()
        how_did_we_get_here = backtrack_path[-1]
        visited[current_room].remove(how_did_we_get_here)
    if len(visited[current_room]) == 0:
        how_did_we_get_here = backtrack_path[-1]
        backtrack_path.pop()
        traversal_path.append(how_did_we_get_here)
        player.travel(how_did_we_get_here)
    else:
        current_direction = visited[current_room][-1]
        visited[current_room].pop()
        traversal_path.append(current_direction)
        backtrack_path.append(backwards_traversal[current_direction])
        player.travel(current_direction)


# TRAVERSAL TEST
visited_rooms = set() 

player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
