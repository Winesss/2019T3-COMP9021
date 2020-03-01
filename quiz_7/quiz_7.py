# COMP9021 19T3 - Rachid Hamadi
# Quiz 7 *** Due Thursday Week 9
#
# Randomly generates a grid of 0s and 1s and determines
# the maximum number of "spikes" in a shape.
# A shape is made up of 1s connected horizontally or vertically (it can contain holes).
# A "spike" in a shape is a 1 that is part of this shape and "sticks out"
# (has exactly one neighbour in the shape).


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for row in grid:
        print('   ', *row) 


# Returns the number of shapes we have discovered and "coloured".
# We "colour" the first shape we find by replacing all the 1s
# that make it with 2. We "colour" the second shape we find by
# replacing all the 1s that make it with 3.
def colour_shapes():
    num_row=len(grid)
    num_column=len(grid[0])
    colour=2
    for i in range(num_row):
        for j in range(num_column):
            if grid[i][j]==1:
                find_continuous_one(i,j,colour)
                colour += 1
    return colour


def max_number_of_spikes(nb_of_shapes):
    num_row = len(grid)
    num_column = len(grid[0])
    dict_colour={}
    for i in range(2,nb_of_shapes+1):
        dict_colour[i]=0
    for n in range(num_row):
        for m in range(num_column):
            if grid[n][m]!=0:
                if find_spike(n,m):
                    dict_colour[grid[n][m]]=dict_colour[grid[n][m]]+1
    num_spikes=dict_colour.values()
    return max(num_spikes)



def find_spike(i,j):
    colour=grid[i][j]
    num_row = len(grid)
    num_column = len(grid[0])
    num_around=0
    if i-1>=0 and grid[i-1][j]==colour:#ahead
        num_around+=1
    if i+1<num_row and grid[i+1][j]==colour:#under
        num_around+=1
    if j-1>=0 and grid[i][j-1]==colour:#left
        num_around+=1
    if j+1<num_column and grid[i][j+1]==colour:#right
        num_around+=1
    if num_around==1:
        return num_around
    else:
        return False




def find_continuous_one(i,j,colour):
    grid[i][j]=colour
    num_row=len(grid)
    num_column=len(grid[0])
    if i-1>=0 and grid[i-1][j]==1:
        find_continuous_one(i-1,j,colour)
    if i+1<num_row and grid[i+1][j]==1:
        find_continuous_one(i+1,j,colour)
    if j-1>=0 and grid[i][j-1]==1:
        find_continuous_one(i,j-1,colour)
    if j+1<num_column and grid[i][j+1]==1:
        find_continuous_one(i,j+1,colour)








try: 
    for_seed, density = (int(x) for x in input('Enter two integers, the second '
                                               'one being strictly positive: '
                                              ).split()
                    )
    if density <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
            for _ in range(dim)
       ]
print('Here is the grid that has been generated:')
display_grid()
nb_of_shapes = colour_shapes()
print('The maximum number of spikes of some shape is:',
      max_number_of_spikes(nb_of_shapes)
     )
