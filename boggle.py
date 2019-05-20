from string import ascii_uppercase
from random import choice

def make_grid(width, height):
    """Create a grid that will hold all the tiles for a boggle game"""
    
    return{(row, col): choice(ascii_uppercase) 
        for row in range(height)
        for col in range(width)
    }

def neighbours_of_a_position(coords):
    """get neighbour of a given position
    """
    row = coords[0]
    col = coords[1]
    
    #Assign each of the neighbours
    
    #Top-left to top-right
    top_left = (row -1, col -1)
    top_center = (row -1, col)
    top_right = (row -1, col +1)
    
    #Middle Left to right
    left = (row, col -1)
    right = (row, col +1)
    
    #Top-left to top-right
    bottom_left = (row +1, col -1)
    bottom_center = (row +1, col)
    bottom_right = (row +1, col +1)
    
    return[top_left, top_center, top_right,
    left, right,
    bottom_left, bottom_center, bottom_right ]

def all_grid_neighbours(grid):
    """get all possible neighbours for each positionin the grid
    """
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_a_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours
        
def path_to_word(grid, path):
    """
    Add all of the letters on the path to a string
    """
    return ''.join([grid[p] for p in path])
    
#ow -te the search function -the function that accepts the grid and the dictionary
"""search throrugh the paths to locate the words by matching strings to words in a dictionary
reason for using paths instead of strings is that a letter could be 
repeated in the grid many times. If we search a word widh a A in it -
how do we know witch A it is? 

Let's write a search function:
"""
def search(grid, dictionary):
    neighbours = all_grid_neighbours(grid)
    paths = []
    #nested function:
    def do_search(path):
        word = path_to_word(grid, path)
        if word in dictionary:
            paths.append(path)
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
    
    for position in grid:
        do_search([position])
        
    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)
    #recursion: a recursive function definierar sig sjarv,
    #in this case search like a tree, neighbors or neighbors of
    #positions

def get_dictionary(dictionary_file):
    """Load dictionary file
    """
    with open(dictionary_file) as f:
        return [w.strip().upper() for w in f]