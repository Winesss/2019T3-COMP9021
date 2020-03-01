# COMP9021 19T3 - Rachid Hamadi
# Quiz 6 *** Due Thursday Week 8
#
# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines move to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines move to the right by one position, e.g.
#      111
#       111
#        111
#         111


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for row in grid:
        print('   ', *row) 


def size_of_largest_parallelogram():
   num_row=len(grid)
   num_columns=len(grid[0])
   current_max=[]
   for i in range(num_row-1):
       for j in range(num_columns-1):
           size = []
           if grid[i][j]==1 and grid[i][j+1]==1:
               length=number_continue(grid,i)
               if find_depth_first(i,j,length):
                   size.append(find_depth_first(i,j,length))
               if find_depth_left(i,j,length):
                   size.append(find_depth_left(i,j,length))
               if find_depth_right(i,j,length):
                   size.append(find_depth_right(i,j,length))
               if size!=[]:
                   current_max.append(max(size))
           else:
               continue
   if current_max!=[]:
       return max(current_max)
   else:
       return False

def find_depth_first(i,j,length):
    num_row = len(grid)
    num_columns = len(grid[0])
    para_area=[]
    for n in range(length,1,-1):
        depth = 0
        x = i
        while x < num_row and j + n <= num_columns:
            if grid[x][j:j + n] == [1]*n:
                depth += 1
                x += 1
            else:
                break
        if depth==1 or depth==0:
            continue
        else:
            para_area.append(depth*n)
    if para_area==[]:
        return False
    else:
        return max(para_area)

def find_depth_left(i,j,length):
    para_area=[]
    num_row = len(grid)
    num_columns = len(grid[0])
    for n in range(length,1,-1):
        depth = 0
        x = i
        y = j
        while x < num_row and y>=0 and y + n <= num_columns:
            if grid[x][y:y + n] == [1]*n:
                depth += 1
                x+= 1
                y-=1
            else:
                break
        if depth==1 or depth==0:
            continue
        else:
            para_area.append(depth*n)
    if para_area==[]:
        return False
    else:
        return max(para_area)

def find_depth_right(i, j, length):
    para_area = []
    num_row = len(grid)
    num_columns = len(grid[0])
    for n in range(length, 1, -1):
        depth = 0
        x = i
        y = j
        while x < num_row and y + n <= num_columns:
            if grid[x][y:y + n] == [1] * n:
                depth += 1
                x += 1
                y += 1
            else:
                break
        if depth == 1 or depth==0:
            continue
        else:
            para_area.append(depth * n)
    if para_area == []:
        return False
    else:
        return max(para_area)


def number_continue(grid,i): #length
    n=0
    list_value=[]
    for k in range(len(grid[0])):
        if grid[i][k]==1:
            n+=1
        else:
            list_value.append(n)
            n=0
            continue
    list_value.append(n)
    return  max(list_value)




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
size = size_of_largest_parallelogram()
if size:
    print('The largest parallelogram with horizontal sides '
          f'has a size of {size}.'
         )
else:
    print('There is no parallelogram with horizontal sides.')
